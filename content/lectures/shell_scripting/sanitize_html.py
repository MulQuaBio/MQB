import re
import sys
from pathlib import Path


NOTEBOOK_PATH_ATTRIBUTE = re.compile(r'\sdata-notebook="[^"]*"')
TRAILING_HORIZONTAL_WHITESPACE = re.compile(r"[ \t]+$", re.MULTILINE)


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} <rendered-html>", file=sys.stderr)
        return 2

    html_path = Path(sys.argv[1])
    if not html_path.is_file():
        print(f"HTML file not found: {html_path}", file=sys.stderr)
        return 2

    html_source = html_path.read_text(encoding="utf-8")
    sanitized_html, removed_count = NOTEBOOK_PATH_ATTRIBUTE.subn("", html_source)
    sanitized_html, whitespace_count = TRAILING_HORIZONTAL_WHITESPACE.subn(
        "", sanitized_html
    )
    if removed_count or whitespace_count:
        html_path.write_text(sanitized_html, encoding="utf-8")

    print(
        f"Removed {removed_count} embedded notebook path attribute(s) and "
        f"normalized trailing whitespace on {whitespace_count} line(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
