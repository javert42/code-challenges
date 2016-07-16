#!/usr/bin/env python
from copy import copy

class Solution(object):
    def __init__(self):
        self.best = []

class Movie(object):
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    def conflicts(self, other):
        if other.start < self.end and other.start > self.start:
            return True
        elif other.end > self.start and other.end < self.end:
            return True
        elif other.start < self.start and self.start < other.end:
            return True
        else:
            return False

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def get_projects():
    return [
        Movie("Tarjan of the Jungle", 7, 24),
        Movie("The President's Algorist", 1, 16),
        Movie("Discrete Mathematics", 3, 13),
        Movie("Steiner's Tree", 20, 30),
        Movie("Halting State", 16, 27),
        Movie("The Four Volume Problem", 29, 50),
        Movie("Programming Challenges", 33, 47),
        Movie("Process Terminated", 44, 57),
        Movie("Calculated Bets", 49, 60),
    ]


def remove_invalid(selected, offered):
    for option in offered[:]:
        for movie in selected:
            if movie.conflicts(option):
                offered.remove(option)


def solve(selected, offered, best):
    remove_invalid(selected, offered)
    if len(offered) + len(selected) < len(best.best):
        return
    if not offered and len(selected) > len(best.best):
        best.best = selected[:]

    for film in offered:
        copy_selected = selected[:]
        copy_selected.append(film)

        copy_offered = offered[:]
        copy_offered.remove(film)

        solve(copy_selected, copy_offered, best)


if __name__ == "__main__":
    solution = Solution() 
    solve([], get_projects(), solution)
    print("Schedule: {}\nIncome: {}".format(solution.best, len(solution.best)))

