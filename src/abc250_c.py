def main():
#     import io
#     import sys

#     _INPUT = """\
# 10 6
# 1
# 5
# 2
# 9
# 6
# 6

#     """
#     sys.stdin = io.StringIO(_INPUT)

    n, q = map(int, input().split())
    a = list(range(1, n + 1))
    d = dict(zip(a, a))
    # key: num, val: idx
    for i in range(q):
        x = int(input())
        # idx = a.index(x)
        idx = d[x]
        if idx == n - 1:
            # a[idx], a[idx - 1] = a[idx - 1], a[idx]
            d[x], a[idx - 1] = a[idx - 1], a[idx]
        else:
            a[idx], a[idx + 1] = a[idx + 1], a[idx]
    print(*a)


main()
