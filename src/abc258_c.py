def main():
#     import io
#     import sys

#     _INPUT = """\
# 10 8
# dsuccxulnl
# 2 4
# 2 7
# 1 2
# 2 7
# 1 1
# 1 2
# 1 3
# 2 5

#     """
#     sys.stdin = io.StringIO(_INPUT)

    shift = 0
    n, q = map(int, input().split())
    s = input()
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            shift = (shift + x) % n
        if t == 2:
            print(s[x - 1 - shift])
        # print(s)


main()
