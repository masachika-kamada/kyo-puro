def main():
    import io
    import sys
    import itertools
    import bisect

#     _INPUT = """\
# 3 600
# 180 240 120

#     """
#     sys.stdin = io.StringIO(_INPUT)

    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    # aの累積和のリストを求める
    a_cumsum = list(itertools.accumulate(a))
    t = t % a_cumsum[-1]
    idx = bisect.bisect_left(a_cumsum, t)
    if idx == 0:
        print(1, t)
    else:
        print(idx + 1, t - a_cumsum[idx - 1])


main()
