#!/usr/bin/env python3

"""Checks for the small functions in control_flow.py."""

from control_flow import (
    count_above,
    even_or_odd,
    find_all_primes,
    is_prime,
    largest_divisor_five,
)


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

# The divisor function returns an integer or None, not display text.
assert largest_divisor_five(120) == 5
assert largest_divisor_five(8) == 4
assert largest_divisor_five(7) is None

# Integers below 2 are not prime; 2 is the first prime.
assert not is_prime(-1)
assert not is_prime(0)
assert not is_prime(1)
assert is_prime(2)
assert is_prime(3)
assert not is_prime(4)
assert find_all_primes(1) == []
assert find_all_primes(10) == [2, 3, 5, 7]

# A normal biological example.
assert count_above([8, 12, 10, 15], 10) == 2

# Values immediately below, at and above the threshold expose > versus >=.
assert count_above([9, 10, 11], 10) == 1

# An empty collection contains no values above the threshold.
assert count_above([], 10) == 0
