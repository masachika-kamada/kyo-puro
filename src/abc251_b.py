def main():
#     import io
#     import sys

#     _INPUT = """\
# 4 12
# 3 3 3 3

#     """
#     sys.stdin = io.StringIO(_INPUT)

    import itertools
    import bisect
    from collections import Counter

    n, w = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    a = [i for i in a if i <= w]
    c = Counter(a)
    c2 = [k for k, v in c.items() if v >= 2]
    c3 = [k for k, v in c.items() if v >= 3]
    a1 = sorted(list(set(a)))
    a2 = a1 + c2
    a3 = a2 + c3
    good_nums = a1

    if n >= 2:
        comb = itertools.combinations(a2, 2)
        comb = list(set(comb))
        comb = sorted([sum(list(i)) for i in comb])
        b = bisect.bisect_right(comb, w)
        good_nums.extend(comb[:b])

    if n >= 3:
        comb = itertools.combinations(a3, 3)
        comb = list(set(comb))
        comb = sorted([sum(list(i)) for i in comb])
        b = bisect.bisect_right(comb, w)
        good_nums.extend(comb[:b])

    print(len(set(good_nums)))
    # print(bisect.bisect_left([1, 2, 3, 4, 5], 4))


main()
