"""
動的計画法を使わないといけないらしい
TODO: 動的計画法(Dynamic Programming)の勉強
"""


import math
import itertools


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def main():
    import io
    import sys

    _INPUT = """\
31 41 592
    """
    sys.stdin = io.StringIO(_INPUT)
    # input = sys.stdin.readline

    n, m, k = map(int, input().split())
    print(n, m, k)
    t = 
    print(combinations_count(k, n) % 998244353)
    # print(list(itertools.combinations(range(m - n), n)))
    # print(list(itertools.combinations(range(5), 3)))


main()
