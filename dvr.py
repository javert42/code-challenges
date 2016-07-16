#!/usr/bin/env python

def print_grid(cols):
    out = ""
    for i, c in enumerate("abcdefghijklmnopqrstuvwxyz"):
        if not i % cols:
            out += "\n"
        out += c + " "
    print(out + "\n")

def solution(cols, word):
    print_grid(cols)
    answer = ""
    for c in word:
        val = ord(c) - ord('a')
        answer += ("d" * (val / cols)) + ("r" * (val % cols)) + "!"
    return answer 

if __name__ == "__main__":
    import sys
    if len(sys.argv) is not 3:
        raise ValueError("Please provide the number of columns and a word.")
    cols = int(sys.argv[1])
    word = sys.argv[2]
    print(solution(cols, word))
    
