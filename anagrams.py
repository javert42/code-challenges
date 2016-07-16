#!/usr/bin/env python
import sys
from collections import defaultdict

def sort_word(word):
    array = list(word)
    array.sort()
    return ''.join(array)

def find_anagrams(word):
    d = defaultdict(list)
    with open("words.txt") as f:
        for line in f.readlines():
            line = line.strip()
            key = sort_word(line)
            d[key].append(line)
    return d[sort_word(word)]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Please provide a word to analyze.")
    word = sys.argv[1]
    print(str(find_anagrams(word)))

