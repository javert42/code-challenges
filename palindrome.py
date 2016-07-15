#!/usr/bin/env python
import sys

def is_palindrome(s):
    """Simple implementation that doesn't consider punctuation, case, etc."""
    end = len(s) - 1
    for start in range(end + 1):
        if s[start] != s[end]:
            return False
        end = end - 1
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("You must pass in a string.")

    s = sys.argv[1]
    print(str(is_palindrome(s)))

