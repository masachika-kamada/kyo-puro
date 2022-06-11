def main():
#     import io
#     import sys

#     _INPUT = """\
# 1 2
# 1 0
# 0 1

#     """
#     sys.stdin = io.StringIO(_INPUT)

    r, c = map(int, input().split())
    a = []
    for i in range(2):
        a.append(list(map(int, input().split())))
    # print(r, c)
    # print(a)
    print(a[r - 1][c - 1])


main()
