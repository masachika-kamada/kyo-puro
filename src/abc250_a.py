def main():
    # import io
    # import sys

    # _INPUT = """\

    # """
    # sys.stdin = io.StringIO(_INPUT)

    h, w = map(int, input().split())
    r, c = map(int, input().split())
    dst = 0

    if h != 1:
        if r > 1:
            dst += 1
        if h - r > 0:
            dst += 1
    if w != 1:
        if c > 1:
            dst += 1
        if w - c > 0:
            dst += 1
    print(dst)


main()
