#!/usr/bin/env python3

"""Functions exemplifying control flow and small, testable units."""

__author__ = 'Your name (your@email.address)'
__version__ = '0.0.1'

import sys

def even_or_odd(x=0):
    """Return a description of whether an integer is even or odd.

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


def count_above(heights_cm, threshold_cm):
    """Return the number of heights strictly above a threshold."""
    above_threshold = 0
    for height_cm in heights_cm:
        if height_cm > threshold_cm:
            above_threshold += 1
    return above_threshold

def largest_divisor_five(x=120):
    """Find which is the largest divisor of x among 2,3,4,5."""
    largest = 0
    if x % 5 == 0:
        largest = 5
    elif x % 4 == 0: #means "else, if"
        largest = 4
    elif x % 3 == 0:
        largest = 3
    elif x % 2 == 0:
        largest = 2
    else: # When all other (if, elif) conditions are not met
        return "No divisor found for %d!" % x # Each function can return a value or a variable.
    return "The largest divisor of %d is %d" % (x, largest)

def is_prime(x=70):
    """Find whether an integer is prime."""
    for i in range(2, x): #  "range" returns a sequence of integers
        if x % i == 0:
          print("%d is not a prime: %d is a divisor" % (x, i)) #Print formatted text "%d %s %f %e" % (20,"30",0.0003,0.00003)

          return False
    print ("%d is a prime!" % x)
    return True 

def find_all_primes(x=22):
    """Find all the primes up to x"""
    allprimes = []
    for i in range(2, x + 1):
      if is_prime(i):
        allprimes.append(i)
    print("There are %d primes between 2 and %d" % (len(allprimes), x))
    return allprimes

def main(argv):
    # sys.exit("don't want to do this right now!")
    print(even_or_odd(22))
    print(even_or_odd(33))
    print(largest_divisor_five(120))
    print(largest_divisor_five(121))
    print(is_prime(60))
    print(is_prime(59))
    print(find_all_primes(100))
    return 0

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)
