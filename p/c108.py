def main():
    n = int(input())
    x = [int(input()) for i in range(n)]

    c = []
    for i in range(n):
        c.append(list(map(int, input().split())))

    k = int(input())
    y = [int(input()) for i in range(k)]

    _from = y[0]
    dst = x[_from - 1]
    print(dst)
    for i in range(1, k):
        _to = y[i]
        dst += c[_from - 1][_to - 1] + x[_to - 1]
        print(c[_from - 1][_to - 1])
        _from = _to
    print(dst)


main()
