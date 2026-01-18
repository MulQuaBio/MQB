"""Custom bibliography formatting for Jupyter Book/Sphinx.

Goal: remove URLs from the rendered reference list unless the entry is clearly a
webpage or software/package reference.

This keeps the BibTeX source intact and applies presentation logic at render
(time) via a custom pybtex formatting style registered as `mqb_nourl`.
"""

from __future__ import annotations

from typing import Any

from pybtex.plugin import register_plugin
from pybtex.richtext import Text
from pybtex.style.formatting.unsrt import Style as UnsrtStyle


def _lower(s: Any) -> str:
    if s is None:
        return ""
    return str(s).lower()


def _is_scholarly(entry: Any) -> bool:
    """Heuristic: treat as scholarly if it looks like a paper/book/report."""
    fields = getattr(entry, "fields", {}) or {}

    # Presence of these fields usually indicates a conventional scholarly item.
    scholarly_fields = {
        "journal",
        "booktitle",
        "publisher",
        "school",
        "institution",
        "volume",
        "number",
        "pages",
        "doi",
        "issn",
        "isbn",
    }
    if any(k in fields for k in scholarly_fields):
        return True

    entry_type = _lower(getattr(entry, "type", ""))
    scholarly_types = {
        "article",
        "book",
        "incollection",
        "inproceedings",
        "proceedings",
        "phdthesis",
        "mastersthesis",
        "techreport",
        "report",
    }
    return entry_type in scholarly_types


def _keep_url(entry: Any) -> bool:
    """Return True iff the URL should be shown in the bibliography."""
    fields = getattr(entry, "fields", {}) or {}

    entry_type = _lower(getattr(entry, "type", ""))
    url = _lower(fields.get("url"))
    title = _lower(fields.get("title"))
    note = _lower(fields.get("note"))
    howpublished = _lower(fields.get("howpublished"))

    if not url:
        return False

    # Strong signals: explicit web/software types.
    if entry_type in {"online", "software"}:
        return True

    # Common software/package indicators.
    software_keywords = {
        "software",
        "package",
        "cran",
        "pypi",
        "conda",
        "bioconductor",
        "github",
        "gitlab",
        "source code",
        "documentation",
        "user guide",
        "manual",
    }
    blob = " ".join([title, note, howpublished, url])
    if any(k in blob for k in software_keywords):
        return True

    # Webpage indicator: has an access date and doesn't look like a paper.
    if "urldate" in fields and not _is_scholarly(entry):
        return True

    return False


class NoUrlUnlessWebOrSoftwareStyle(UnsrtStyle):
    """unsrt-like references, but suppress URLs for non-web/software items."""

    def format_url(self, e: Any) -> Text:  # pybtex uses `e` for the entry
        if not _keep_url(e):
            return Text("")

        # Prefer the base style's formatting if available.
        try:
            return super().format_url(e)
        except Exception:
            url = (getattr(e, "fields", {}) or {}).get("url")
            if not url:
                return Text("")
            return Text(url)

    def format_urldate(self, e: Any) -> Text:
        # Only show access dates when we show the URL.
        if not _keep_url(e):
            return Text("")
        try:
            return super().format_urldate(e)
        except Exception:
            return Text("")


def setup(app: Any) -> dict[str, Any]:
    # Register our style under a simple name.
    register_plugin(
        "pybtex.style.formatting",
        "mqb_nourl",
        NoUrlUnlessWebOrSoftwareStyle,
    )

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
