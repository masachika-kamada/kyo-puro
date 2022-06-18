def main():
#     import io
#     import sys

#     _INPUT = """\
# 10
# 2 2 4 1 1 1 4 2 2 1

#     """
#     sys.stdin = io.StringIO(_INPUT)

    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()

    from itertools import accumulate
    accumulate_a = list(accumulate(a))
    # print(accumulate_a)
    import bisect
    idx = bisect.bisect_right(accumulate_a, 3)
    # print(idx)
    print(n - idx)


main()
