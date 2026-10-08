#!/usr/bin/env python3

"""Checks for the small functions in control_flow.py."""

from control_flow import count_above, even_or_odd


# Normal cases: representative even and odd integers.
assert even_or_odd(10) == "10 is Even!"
assert even_or_odd(5) == "5 is Odd!"

# Edge cases: zero and a negative integer remain valid inputs.
assert even_or_odd(0) == "0 is Even!"
assert even_or_odd(-2) == "-2 is Even!"

# Failure case: the function's contract requires an integer.
try:
    even_or_odd("10")
except TypeError:
    pass
else:
    raise AssertionError("A non-integer input was accepted")

# A normal biological example.
assert count_above([8, 12, 10, 15], 10) == 2

# Values immediately below, at and above the threshold expose > versus >=.
assert count_above([9, 10, 11], 10) == 1

# An empty collection contains no values above the threshold.
assert count_above([], 10) == 0
