import itertools


def main():
#     import io
#     import sys

#     _INPUT = """\
# 4 2
# abii
# aef
# bc
# acg

#     """
#     sys.stdin = io.StringIO(_INPUT)

    n, k = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    a = list("".join(s))
    a = list(set(a))

    cnt = 0
    for i in range(n + 1):
        comb = itertools.combinations(s, i)
        for c in comb:
            c = "".join(c)
            count = 0
            for ch in a:
                if c.count(ch) == k:
                    count += 1
            if count > cnt:
                cnt = count

    print(cnt)


main()
