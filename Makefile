.PHONY: init test

# Create/update the local virtualenv and install Python dependencies
init:
	bash scripts/bootstrap.sh

# "Test" for this repository = build the Jupyter Book locally
test:
	. .venv/bin/activate && jupyter-book build content
