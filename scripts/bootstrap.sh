#!/usr/bin/env bash
set -euo pipefail

# Create (or reuse) a per-project virtual environment in .venv/
python3 -m venv .venv

# Activate it for the remainder of this script
# shellcheck disable=SC1091
source .venv/bin/activate

requirements_file="${REQUIREMENTS_FILE:-requirements.txt}"
if [[ ! -f "$requirements_file" ]]; then
	printf 'requirements file not found: %s\n' "$requirements_file" >&2
	exit 1
fi

python -m pip install --upgrade pip setuptools wheel
python -m pip install -r "$requirements_file"

echo "ready: virtualenv created at .venv/ and requirements installed."
