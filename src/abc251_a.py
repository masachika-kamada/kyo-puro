def main():
#     import io
#     import sys

#     _INPUT = """\
# z
#     """
#     sys.stdin = io.StringIO(_INPUT)

    s = input()
    a = int(6 / len(s))
    res = ""
    for i in range(a):
        res += s
    print(res)


main()
