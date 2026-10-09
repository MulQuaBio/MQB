#!/usr/bin/env python3

"""Display the command-line arguments supplied to this program."""

import sys


def main():
    """Report the script name and its command-line arguments."""
    print(f"Script name: {sys.argv[0]}")
    print(f"Number of arguments: {len(sys.argv) - 1}")
    print(f"Arguments: {sys.argv[1:]}")


if __name__ == "__main__":
    main()
