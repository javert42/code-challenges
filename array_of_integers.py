#!/usr/bin/env python


def find_solution(numbers):
    last = None
    values = []
    longest = []
    for value in numbers:
        if value > last:
            values.append(value)
            last = value
        else:
            if len(values) > len(longest):
                longest = values
            last = None
            values = [value]
    if len(values) > len(longest):
        longest = values
    return longest

if __name__ == "__main__":
    import sys
    if len(sys.argv) is not 2:
        sys.stderr.write("Please a string of numbers.")
    numbers = map(int, sys.argv[1].split(' '))
    print(find_solution(numbers))

