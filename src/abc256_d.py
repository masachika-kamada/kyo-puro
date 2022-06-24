def main():
#     import io
#     import sys

#     _INPUT = """\
# 3
# 10 20
# 20 30
# 40 50

#     """
#     sys.stdin = io.StringIO(_INPUT)

    lrs = []
    n = int(input())
    for _ in range(n):
        lr = list(map(int, input().split()))
        lrs.append(lr)
    lrs.sort()
    lrs.append([10 ** 6, 10 ** 6])
    l_min, r_max = lrs[0]

    for l, r in lrs[1:]:
        if l > r_max:
            print(l_min, r_max)
            l_min, r_max = l, r
        elif r > r_max:
            r_max = r


main()
