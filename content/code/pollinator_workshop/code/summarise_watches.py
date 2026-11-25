"""Summarise timed pollinator watches by site."""

import argparse
import csv
import sys
from pathlib import Path


FIELDS = ("site", "watch_id", "status", "minutes", "visits")


def read_watches(path):
    with Path(path).open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream, strict=True)
        if tuple(reader.fieldnames or ()) != FIELDS:
            raise ValueError("expected site,watch_id,status,minutes,visits")
        seen = set()
        for line, row in enumerate(reader, start=2):
            try:
                site, watch_id, status, minutes, visits = (
                    row[field].strip() for field in FIELDS
                )
                if None in row or not site or not watch_id or watch_id in seen:
                    raise ValueError("check the columns, site and unique watch ID")
                minutes = int(minutes)
                if minutes <= 0:
                    raise ValueError("watch duration must be positive")
                if status == "cancelled" and visits == "":
                    visits = None
                elif status == "completed":
                    visits = int(visits)
                    if visits < 0:
                        raise ValueError("visit count must be non-negative")
                else:
                    raise ValueError("check the status and visit count")
            except (AttributeError, ValueError) as error:
                raise ValueError(f"row {line}: {error}") from error
            seen.add(watch_id)
            yield site, status, minutes, visits


def summarise(watches):
    totals = {}
    for site, status, minutes, visits in watches:
        total = totals.setdefault(site, {"observed_minutes": 0, "visits": 0})
        if status == "completed":
            total["observed_minutes"] += minutes
            total["visits"] += visits
    return totals


def pooled_rate(visits, observed_minutes):
    if observed_minutes == 0:
        return None
    return visits / observed_minutes


def write_report(totals, stream):
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(["site", "visits_per_minute"])
    for site, total in sorted(totals.items()):
        rate = pooled_rate(total["visits"], total["observed_minutes"])
        writer.writerow([site, rate])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="CSV of timed watches")
    args = parser.parse_args()
    try:
        totals = summarise(read_watches(args.input))
    except (OSError, ValueError, csv.Error) as error:
        parser.exit(2, f"{error}\n")
    write_report(totals, sys.stdout)


if __name__ == "__main__":
    main()
