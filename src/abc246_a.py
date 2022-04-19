def a(l):
    a, b, c = l
    if a == b:
        return c
    elif b == c:
        return a
    else:
        return b


def main():
    # import io
    # import sys

    # _INPUT = """\

    # """
    # sys.stdin = io.StringIO(_INPUT)
    # input = sys.stdin.readline

    x = []
    y = []

    for _ in range(3):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
    X = a(x)
    Y = a(y)
    print(X, Y)


main()
