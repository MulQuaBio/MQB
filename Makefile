.PHONY: init test check-content

# Create/update the local virtualenv and install python dependencies
init:
	bash scripts/bootstrap.sh

# "Test" for this repository = build the Jupyter Book locally
test: check-content
	. .venv/bin/activate && PYTHONPATH=$(CURDIR) jupyter-book build content

check-content:
	.venv/bin/python -m unittest discover -s scripts -p 'test_check_content.py'
	.venv/bin/python scripts/check_content.py
