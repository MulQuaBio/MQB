"""Import shim for the custom Sphinx extension.

Jupyter Book builds run Sphinx with the book source folder (this directory)
added to ``sys.path``.

The actual extension code lives in ``content/_ext/mqb_bibstyle.py``. This shim
makes it importable as ``mqb_bibstyle`` (as referenced in ``content/_config.yml``)
without needing additional Sphinx path configuration.
"""

from _ext.mqb_bibstyle import *  # noqa: F401,F403
