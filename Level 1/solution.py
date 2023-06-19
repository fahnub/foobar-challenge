from math import sqrt


def get_factors(n):
    factors = set()

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors.update([i, n//i])

    return sorted(factors)


def get_substrings(s):
    substrings = []

    for factor in get_factors(len(s)):
        substrings.append(s[0: factor])

    return substrings


def solution(s):
    if len(s) == 1:
        return 1

    if s.count(s[0]) == 1:
        return 1

    if s.index(s[0], 1) > len(s) / 2:
        return 1

    substrings = get_substrings(s)

    for substring in substrings:
        if s.count(substring) * len(substring) == len(s):
            return s.count(substring)
