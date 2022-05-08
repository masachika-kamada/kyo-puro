def main():
#     import io
#     import sys

#     _INPUT = """\
# 1 4 4

#     """
#     sys.stdin = io.StringIO(_INPUT)

    n, a, b = map(int, input().split())

    for h in range(n):
        if h % 2 == 0:
            flag = True
        else:
            flag = False
        c = ""
        flag = not flag
        for w in range(n):
            for _w in range(b):
                if flag is False:
                    c += "."
                else:
                    c += "#"
            flag = not flag
        for _h in range(a):
            print(c)


main()
