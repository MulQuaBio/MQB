# Algorithms practical: measured example

Measured on 27 October 2026 using the public lecture's two correct 2-SUM
functions and the timing scaffold supplied with the algorithms chapter.
These are actual elapsed-time measurements, not synthetic target ratios.

- Input: shuffled distinct integers `-m, ..., -1, 1, ..., m`, with `n = 2m`.
  The independently expected count is `m`. Both algorithms receive the same list.
- Sizes: 128, 256, 512, 1024; random seed 20261027, using `Random(seed + n)`.
- Method: one untimed warm-up, five timed calls, median elapsed seconds from
  `time.perf_counter`. Input construction, correctness checks and output writing
  are outside the timer. Brute force is measured before the set at each size.
- Runtime: CPython 3.14.4, Linux 7.0.0-38-generic, glibc 2.43, x86_64.
- CPU: Intel Core Ultra 5 335. Other system activity was not controlled.
- `doubling_ratio` divides the median by the previous median for the same
  algorithm; the first ratio is blank. The short durations are sensitive to
  clock resolution, interpreter effects and background activity.

To make a new table, complete the two functions in
`code/algorithms_compare_starter.py` and run from your project root:

```bash
python3 code/algorithms_compare_starter.py
```

The result is `results/algorithms_timings.csv`. Exact times will vary. Use these
data to assess evidence for quadratic versus expected-linear growth, explain
departures from exact doubling predictions, and discuss the extra memory.
The metadata columns in the CSV describe this measurement environment.
