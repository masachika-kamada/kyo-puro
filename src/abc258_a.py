def main():
    # import io
    # import sys

    # _INPUT = """\

    # """
    # sys.stdin = io.StringIO(_INPUT)

    k = int(input())
    h = k // 60
    h = str((21 + h) % 24)
    m = str(k % 60)
    if len(m) == 1:
        m = "0" + m
    if len(h) == 1:
        h = "0" + h
    print(h + ":" + m)


main()
