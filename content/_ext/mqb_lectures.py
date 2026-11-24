"""Copy standalone Quarto decks without flattening their book URLs."""

from pathlib import Path
from shutil import copy2

DECKS = (
    Path("lectures/algorithms/algorithms.html"),
    Path("lectures/ai_coding/ai_coding.html"),
)


def copy_lectures(app, exception):
    if exception is not None or app.builder.format != "html":
        return
    for relative in DECKS:
        source = Path(app.srcdir) / relative
        destination = Path(app.outdir) / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        copy2(source, destination)


def setup(app):
    app.connect("build-finished", copy_lectures)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}
