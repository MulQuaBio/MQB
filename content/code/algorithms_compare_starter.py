#!/usr/bin/env python3
"""Compare two distinct-integer 2-SUM algorithms.

Complete the two marked functions, add an independently worked small case, then
run from your project root: python3 code/algorithms_compare_starter.py
The standard-library scaffold supplies input construction, timing and CSV output.
"""

import argparse
import csv
import platform
import random
import sys
from pathlib import Path
from statistics import median
from time import perf_counter


def count_two_sum_brute(values: list[int]) -> int:
    """Count pairs i < j summing to zero in distinct integers; preserve input."""
    # TODO: implement the all-pairs algorithm from the chapter.
    raise NotImplementedError("Complete count_two_sum_brute before timing.")


def count_two_sum_set(values: list[int]) -> int:
    """Count the same pairs using a set of earlier values; preserve input."""
    # TODO: implement the set algorithm from the chapter.
    raise NotImplementedError("Complete count_two_sum_set before timing.")


def check_small_cases(functions):
    """Check shared expectations independently of the timing experiment."""
    cases = [
        ([], 0),
        ([0], 0),
        ([-2, 5, 2], 1),
        ([-3, 0, 3], 1),
        ([3, -3, 5, 8, -8], 2),
        # TODO: add one independently worked case and explain its purpose.
    ]
    for name, function in functions.items():
        for values, expected in cases:
            original = values.copy()
            actual = function(values)
            if actual != expected:
                raise AssertionError(f"{name}: {values} gave {actual}, expected {expected}")
            if values != original:
                raise AssertionError(f"{name} modified its input")


def make_input(n, seed):
    """Return n distinct nonzero integers, with independently known n // 2 pairs."""
    if n < 2 or n % 2:
        raise ValueError("Input size must be an even integer of at least two.")
    m = n // 2
    values = list(range(-m, 0)) + list(range(1, m + 1))
    random.Random(seed + n).shuffle(values)
    return values


def elapsed_seconds(function, values, expected, repetitions):
    """Median elapsed seconds; checks and preparation stay outside the timer."""
    original = values.copy()
    if function(values) != expected:  # untimed warm-up and correctness check
        raise AssertionError("Warm-up returned an incorrect answer.")
    if values != original:
        raise AssertionError("Warm-up modified its input.")
    times = []
    for _ in range(repetitions):
        start = perf_counter()
        actual = function(values)
        elapsed = perf_counter() - start
        if actual != expected:
            raise AssertionError("A measured call returned an incorrect answer.")
        if values != original:
            raise AssertionError("A measured call modified its input.")
        times.append(elapsed)
    return median(times)


def collect_timings(functions, sizes, repetitions=5, seed=20261027):
    """Use the same prepared input for both algorithms at each size."""
    if repetitions < 5:
        raise ValueError("Use at least five measured repetitions.")
    if not sizes or any(b != 2 * a for a, b in zip(sizes, sizes[1:])):
        raise ValueError("Use a non-empty series of successively doubled sizes.")
    rows = []
    previous = {}
    for n in sizes:
        values = make_input(n, seed)  # outside the timer
        expected = n // 2
        for name, function in functions.items():
            seconds = elapsed_seconds(function, values, expected, repetitions)
            prior = previous.get(name)
            ratio = "" if prior is None or prior == 0 else seconds / prior
            rows.append({
                "n": n,
                "algorithm": name,
                "expected_pairs": expected,
                "median_seconds": seconds,
                "doubling_ratio": ratio,
                "repetitions": repetitions,
                "seed": seed,
                "python": platform.python_version(),
                "platform": platform.platform(),
                "machine": platform.machine(),
                "timer": "perf_counter",
            })
            previous[name] = seconds
    return rows


def write_timings(rows, output):
    """Write a reproducible results table after the experiment has finished."""
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sizes", nargs="+", type=int, default=[128, 256, 512, 1024])
    parser.add_argument("--repetitions", type=int, default=5)
    parser.add_argument("--seed", type=int, default=20261027)
    parser.add_argument("--output", type=Path, default=Path("results/algorithms_timings.csv"))
    args = parser.parse_args()
    functions = {"brute": count_two_sum_brute, "set": count_two_sum_set}
    try:
        check_small_cases(functions)
        rows = collect_timings(functions, args.sizes, args.repetitions, args.seed)
    except (NotImplementedError, ValueError, AssertionError) as error:
        parser.exit(1, f"{error}\n")
    write_timings(rows, args.output)
    print(f"Checks passed. Wrote {len(rows)} timing rows to {args.output}")
    print(f"Python {platform.python_version()}; {platform.platform()}; {platform.machine()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
