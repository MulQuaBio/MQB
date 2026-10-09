#!/usr/bin/env python3

"""Demonstrate the value Python assigns to __name__."""


def module_name():
    """Return the name Python assigned to this module."""
    return __name__


def main():
    """Report the module name during direct execution."""
    print(f"This module's name is: {module_name()}")


if __name__ == "__main__":
    main()
