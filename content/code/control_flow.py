#!/usr/bin/env python3

"""Small, reusable functions that demonstrate control flow."""


def even_or_odd(x):
    """Return a description of whether integer x is even or odd.

    >>> even_or_odd(10)
    '10 is Even!'
    >>> even_or_odd(5)
    '5 is Odd!'
    >>> even_or_odd(-2)
    '-2 is Even!'
    """
    if not isinstance(x, int):
        raise TypeError("x must be an integer")
    if x % 2 == 0:
        return f"{x} is Even!"
    return f"{x} is Odd!"


def largest_divisor_five(x):
    """Return the largest divisor of x among 2, 3, 4 and 5, or None."""
    if not isinstance(x, int):
        raise TypeError("x must be an integer")
    for divisor in (5, 4, 3, 2):
        if x % divisor == 0:
            return divisor
    return None


def is_prime(x):
    """Return True when integer x is prime, and False otherwise."""
    if not isinstance(x, int):
        raise TypeError("x must be an integer")
    if x < 2:
        return False
    for divisor in range(2, x):
        if x % divisor == 0:
            return False
    return True


def find_all_primes(limit):
    """Return a list of all prime integers from 2 through limit."""
    if not isinstance(limit, int):
        raise TypeError("limit must be an integer")
    return [number for number in range(2, limit + 1) if is_prime(number)]


def count_above(heights_cm, threshold_cm):
    """Return the number of heights strictly above a threshold."""
    count = 0
    for height_cm in heights_cm:
        if height_cm > threshold_cm:
            count += 1
    return count


def main():
    """Display representative results from the functions above."""
    print(even_or_odd(22))
    print(even_or_odd(33))
    print(f"Largest divisor among 2, 3, 4 and 5: {largest_divisor_five(120)}")
    print(f"Is 59 prime? {is_prime(59)}")
    print(f"Primes up to 20: {find_all_primes(20)}")


if __name__ == "__main__":
    main()
