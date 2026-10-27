"""Copy the standalone algorithms deck without flattening its book URL."""

from pathlib import Path
from shutil import copy2


def copy_algorithms_lecture(app, exception):
    if exception is not None or app.builder.format != "html":
        return
    relative = Path("lectures/algorithms/algorithms.html")
    source = Path(app.srcdir) / relative
    destination = Path(app.outdir) / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    copy2(source, destination)


def setup(app):
    app.connect("build-finished", copy_algorithms_lecture)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}
