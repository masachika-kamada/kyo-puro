def main():
#     import io
#     import sys

#     _INPUT = """\
# 3
#     """
#     sys.stdin = io.StringIO(_INPUT)

    n = int(input())
    for i in range(n, -1, -1):
        print(i)


main()
