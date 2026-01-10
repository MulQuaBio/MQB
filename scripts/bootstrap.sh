#!/usr/bin/env bash
set -euo pipefail

# Create (or reuse) a per-project virtual environment in .venv/
python3 -m venv .venv

# Activate it for the remainder of this script
# shellcheck disable=SC1091
source .venv/bin/activate

python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt

echo "ready: virtualenv created at .venv/ and requirements installed."
