"""Run hand-derived checks from the workshop project root."""

import argparse
import csv
import io
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCRIPT = ROOT / "code" / "summarise_watches.py"


def run(script, name):
    return subprocess.run(
        [sys.executable, str(script), str(ROOT / "data" / name)],
        check=False,
        capture_output=True,
        text=True,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("script", nargs="?", type=Path, default=DEFAULT_SCRIPT)
    parser.add_argument("--show-minutes", action="store_true")
    args = parser.parse_args()

    result = run(args.script, "pollinator_watches.csv")
    assert result.returncode == 0, result.stderr
    table = csv.DictReader(io.StringIO(result.stdout))
    columns = ["site", "visits_per_minute"]
    if args.show_minutes:
        columns.insert(1, "observed_minutes")
    assert table.fieldnames == columns, table.fieldnames
    records = list(table)
    assert [row["site"] for row in records] == ["Hedge", "Meadow", "Wood"], records
    rows = {row["site"]: row for row in records}
    assert math.isclose(float(rows["Hedge"]["visits_per_minute"]), 2 / 10)
    assert math.isclose(float(rows["Meadow"]["visits_per_minute"]), 3 / 15), rows
    assert rows["Wood"]["visits_per_minute"] == "", rows
    if args.show_minutes:
        assert [int(row["observed_minutes"]) for row in records] == [10, 15, 0]

    invalid = run(args.script, "invalid_watches.csv")
    assert invalid.returncode != 0 and not invalid.stdout, invalid
    assert "row 3" in invalid.stderr, invalid.stderr
    assert run(args.script, "pollinator_watches.csv").stdout == result.stdout
    print("The report matches the hand-checked rates, missing rate and repeat run.")
    print("The invalid row was rejected.")


if __name__ == "__main__":
    main()
