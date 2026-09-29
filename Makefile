.PHONY: init test check-content

# Create/update the local virtualenv and install python dependencies
init:
	bash scripts/bootstrap.sh

# "Test" for this repository = build the Jupyter Book locally
test:
	. .venv/bin/activate && PYTHONPATH=$(CURDIR) jupyter-book build content

check-content:
	.venv/bin/python scripts/check_content.py
