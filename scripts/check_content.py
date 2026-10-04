"""Report broken local references in the published Jupyter Book sources."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import nbformat
import yaml
from markdown_it import MarkdownIt


SOURCE_EXTENSIONS = (".md", ".ipynb")
LOCAL_PATH = re.compile(r"(?<![\w/])(?:\.\./|\./)+(?:[Dd]ata|[Cc]ode|[Rr]esults)/[\w./-]+")
MARKDOWN = MarkdownIt()


def book_pages(book: Path) -> tuple[list[Path], list[str]]:
    toc = yaml.safe_load((book / "_toc.yml").read_text(encoding="utf-8"))
    pages = []
    problems = []

    def visit(entry: dict) -> None:
        if "root" in entry:
            visit({"file": entry["root"]})
        if "file" in entry:
            stem = book / entry["file"]
            candidates = [stem] if stem.suffix else [stem.with_suffix(ext) for ext in SOURCE_EXTENSIONS]
            matches = [candidate for candidate in candidates if candidate.is_file()]
            if not matches:
                problems.append(f"_toc.yml: missing page {entry['file']}")
            else:
                pages.append(matches[0])
        for key in ("parts", "chapters", "sections"):
            for child in entry.get(key, []):
                visit(child)

    visit(toc)
    return pages, problems


def old_names(ledger: Path) -> set[str]:
    names = set()
    for line in ledger.read_text(encoding="utf-8").splitlines():
        previous, current = line.split("\t", 1)
        previous_name = Path(previous).name
        current_name = Path(current).name
        if (
            previous.startswith("content/data/")
            and previous_name != current_name
        ):
            names.add(previous_name)
    return names


def local_target(source: Path, book: Path, url: str) -> Path | None:
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc or url.startswith("#"):
        return None
    path = unquote(parsed.path)
    if not path or ("/" not in path and not Path(path).suffix and not path.startswith(".")):
        return None
    return (book / path.lstrip("/")) if path.startswith("/") else (source.parent / path)


def exists_as_source(path: Path) -> bool:
    if path.is_file():
        return True
    return not path.suffix and any(path.with_suffix(ext).is_file() for ext in SOURCE_EXTENSIONS)


def check_text(source: Path, book: Path, text: str, location: str, names: set[str], *, code: bool = False) -> list[str]:
    problems = []
    tokens = MARKDOWN.parse(text)
    for token in tokens:
        if token.type != "inline":
            continue
        for child in token.children or []:
            if child.type not in ("link_open", "image"):
                continue
            url = child.attrGet("href" if child.type == "link_open" else "src")
            if url and (target := local_target(source, book, url)) and not exists_as_source(target):
                problems.append(f"{location}: missing link {url}")

    if code:
        for match in LOCAL_PATH.finditer(text):
            reference = match.group().rstrip(".,;:)")
            if "/results/" in reference.lower():
                continue
            target = (source.parent / reference)
            if not target.is_file():
                problems.append(f"{location}: missing exact-case path {reference}")

    for name in names:
        if re.search(rf"(?<![\w.-]){re.escape(name)}(?![\w.-])", text):
            problems.append(f"{location}: old data filename {name}")
    return problems


def check_book(book: Path, ledger: Path) -> list[str]:
    pages, problems = book_pages(book)
    names = old_names(ledger)
    for page in pages:
        relative = page.relative_to(book)
        if page.suffix == ".md":
            problems.extend(check_text(page, book, page.read_text(encoding="utf-8"), str(relative), names))
            continue
        try:
            notebook = nbformat.read(page, as_version=4)
        except (ValueError, OSError) as error:
            problems.append(f"{relative}: invalid notebook: {error}")
            continue
        try:
            nbformat.validate(notebook, relax_add_props=True)
        except nbformat.ValidationError as error:
            problems.append(f"{relative}: invalid notebook: {error.message}")
        if any(cell.cell_type == "code" for cell in notebook.cells) and not notebook.metadata.get("kernelspec", {}).get("name"):
            problems.append(f"{relative}: missing kernel name")
        for index, cell in enumerate(notebook.cells, start=1):
            if cell.cell_type in ("markdown", "code"):
                problems.extend(check_text(page, book, cell.source, f"{relative}:cell {index}", names,
                                           code=cell.cell_type == "code"))
    return sorted(set(problems))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--book", type=Path, default=Path("content"))
    parser.add_argument("--ledger", type=Path, default=Path("results/rename_mapping_applied.tsv"))
    args = parser.parse_args()
    problems = check_book(args.book, args.ledger)
    for problem in problems:
        print(problem)
    print(f"Content check: {len(problems)} issue(s)")
    return bool(problems)


if __name__ == "__main__":
    raise SystemExit(main())