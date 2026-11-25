"""Build the live and Git self-study packs from the chapter's exercises."""

import difflib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from markdown_it import MarkdownIt


CONTENT = Path(__file__).resolve().parents[1] / "content"
SOURCE = CONTENT / "code" / "pollinator_workshop"
NOTEBOOK = CONTENT / "notebooks" / "ai-assisted-programming.ipynb"
OUTPUT = CONTENT / "data" / "workshop_ai_pollinators.zip"
GIT_OUTPUT = CONTENT / "data" / "workshop_ai_git.zip"
BOOK = "https://mulquabio.github.io/MQB/notebooks"
SCRIPT = "code/summarise_watches.py"
CHECK = "checks/check_watches.py"
MEADOW = "data/pollinator_watches.csv"
TRANSFER = "data/transfer_watches.csv"


def replace_once(source, old, new):
    if source.count(old) != 1:
        raise ValueError(f"Practice scaffold changed around: {old}")
    return source.replace(old, new)


def candidates(source):
    yield "replay/counts_cancelled_minutes.py", replace_once(
        source,
        '        if status == "completed":\n            total["observed_minutes"] += minutes',
        '        total["observed_minutes"] += minutes\n        if status == "completed":',
    )
    yield "replay/report_with_minutes.py", replace_once(
        replace_once(
            source,
            'writer.writerow(["site", "visits_per_minute"])',
            'writer.writerow(["site", "observed_minutes", "visits_per_minute"])',
        ),
        "writer.writerow([site, rate])",
        'writer.writerow([site, total["observed_minutes"], rate])',
    )
    yield "replay/transfer_candidate.py", replace_once(
        source, "        return None\n", "        return 0.0\n"
    )


def task_html(flag, title, count):
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    exercises = []
    for cell in notebook["cells"]:
        if cell.get("metadata", {}).get(flag):
            lines = cell["source"]
            exercises.append("".join(line for line in lines if not line.rstrip().endswith(")=")))
    if len(exercises) != count:
        raise ValueError(f"Expected {count} exercises under {flag}")
    text = "\n\n".join(exercises)
    if flag == "mqb_git_card":
        text = text.replace("(git.ipynb)", f"({BOOK}/git.html)")
        text = text.replace(
            "Download the {download}`pollinator Git practice repository <../data/workshop_ai_git.zip>`.\n"
            "Extract it into a new directory and open the extracted `pollinator-git` folder.",
            "Open this extracted `pollinator-git` folder.",
        )
        text = text.replace(
            "{ref}`original rule <ai-live-remember>`",
            f"[original rule]({BOOK}/ai-assisted-programming.html#ai-live-remember)",
        )
    markdown = MarkdownIt("commonmark", {"html": True}).enable("table")
    return (
        '<!doctype html><html lang="en-GB"><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        f'<title>{title} · MQB</title>'
        '<style>body{font:1rem/1.6 system-ui;max-width:54rem;margin:2rem auto;padding:0 1rem}'
        'pre{overflow:auto;background:#f2f4f5;padding:1rem}summary{cursor:pointer}'
        'th,td{border-bottom:1px solid #aaa;padding:.3rem .7rem;text-align:left}</style>'
        f'<main><h1>{title}</h1>'
        '<p>Offline copy of the task from the MQB chapter '
        '<a href="https://mulquabio.github.io/MQB/notebooks/ai-assisted-programming.html">'
        'AI-assisted programming in biology</a>. <a href="NOTICE.md">Credits and licence</a>.</p>'
        + markdown.render(text)
        + "</main></html>\n"
    )


def run_replay(folder):
    commands = [
        [SCRIPT, MEADOW],
        [CHECK],
        [CHECK, "replay/report_with_minutes.py", "--show-minutes"],
        ["replay/report_with_minutes.py", MEADOW],
    ]
    entries = ["MQB teaching replay. These are local Python command results.\n"]
    for args in commands:
        result = subprocess.run(
            [sys.executable, *args], cwd=folder, capture_output=True, text=True, check=True
        )
        entries.extend([f"$ python {' '.join(args)}", result.stdout.rstrip(), ""])
    return "\n".join(entries)


def write_files(folder, files):
    for name, data in files.items():
        path = folder / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)


def write_archive(output, files):
    temporary = output.with_suffix(".zip.partial")
    try:
        with ZipFile(temporary, "w") as archive:
            for name, data in sorted(files.items()):
                entry = ZipInfo(name, date_time=(2026, 11, 25, 0, 0, 0))
                entry.external_attr = 0o100644 << 16
                archive.writestr(entry, data, compress_type=ZIP_DEFLATED)
        os.replace(temporary, output)
    finally:
        temporary.unlink(missing_ok=True)
    print(output)


def build_git_pack(files, report_candidate):
    git_files = {name: data for name, data in files.items() if name not in {"README.md", TRANSFER}}
    git_files["task.html"] = task_html("mqb_git_card", "AI-assisted version control", 1).encode()
    git_files["README.md"] = (
        "# Pollinator Git practice\n\n"
        "Open task.html for the exercise. This folder already contains a local\n"
        "Git repository with one commit and two changes to review. Start with\n"
        "git status from this folder. Leave it separate from your other projects.\n"
    ).encode()
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update({
        "GIT_CONFIG_GLOBAL": os.devnull,
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_AUTHOR_NAME": "MQB teaching example",
        "GIT_AUTHOR_EMAIL": "practice@example.invalid",
        "GIT_AUTHOR_DATE": "2026-11-25T14:00:00+00:00",
        "GIT_COMMITTER_NAME": "MQB teaching example",
        "GIT_COMMITTER_EMAIL": "practice@example.invalid",
        "GIT_COMMITTER_DATE": "2026-11-25T14:00:00+00:00",
    })
    with tempfile.TemporaryDirectory(prefix="mqb-pollinator-git-") as work:
        repo = Path(work) / "pollinator-git"
        write_files(repo, git_files)

        def git(*args):
            return subprocess.check_output(["git", *args], cwd=repo, env=env, text=True)

        git("init", "--quiet", "--initial-branch=main", "--template=")
        git("config", "core.filemode", "false")
        git("add", "--", *git_files)
        git("commit", "--quiet", "-m", "Add pollinator watch practice baseline")
        changed = replace_once(
            report_candidate,
            '        if status == "completed":',
            '        if status == "completed" and visits > 0:',
        )
        (repo / SCRIPT).write_text(changed, encoding="utf-8")
        patch = git("diff", "--", SCRIPT)
        if patch.count("\n@@ ") != 2 or git("diff", "--staged", "--", SCRIPT):
            raise ValueError("Expected two separate unstaged hunks in the Git pack")
        git_files[SCRIPT] = changed.encode()
        for metadata in (repo / ".git").rglob("*"):
            if metadata.is_file():
                git_files[metadata.relative_to(repo).as_posix()] = metadata.read_bytes()
        write_archive(GIT_OUTPUT, {f"pollinator-git/{name}": data for name, data in git_files.items()})


def main():
    sources = ["README.md", "NOTICE.md", SCRIPT, CHECK, MEADOW, TRANSFER, "data/invalid_watches.csv"]
    files = {name: (SOURCE / name).read_bytes() for name in sources}
    files["LICENSE"] = (CONTENT.parent / "LICENSE").read_bytes()
    files["CC-BY-4.0.txt"] = (CONTENT / "images" / "ai-coding" / "CC-BY-4.0.txt").read_bytes()
    source = files[SCRIPT].decode()
    prepared = dict(candidates(source))
    report_candidate = prepared["replay/report_with_minutes.py"]
    build_git_pack(files, report_candidate)
    files.update({name: data.encode() for name, data in prepared.items()})
    patch = difflib.unified_diff(
        source.splitlines(keepends=True), report_candidate.splitlines(keepends=True),
        fromfile=f"a/{SCRIPT}", tofile=f"b/{SCRIPT}",
    )
    files["replay/report_with_minutes.diff"] = "".join(patch).encode()
    files["task.html"] = task_html("mqb_offline_card", "Pollinator watches", 7).encode()
    with tempfile.TemporaryDirectory(prefix="mqb-pollinator-replay-") as work:
        folder = Path(work)
        write_files(folder, files)
        files["replay/command-output.txt"] = run_replay(folder).encode()
    write_archive(OUTPUT, files)


if __name__ == "__main__":
    main()
