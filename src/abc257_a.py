def main():
#     import io
#     import sys

#     _INPUT = """\
# 2 3

#     """
#     sys.stdin = io.StringIO(_INPUT)

    n, x = map(int, input().split())
    idx = -(-x // n)
    print(chr(96 + idx).upper())


main()
