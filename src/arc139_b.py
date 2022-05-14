def main():
    import io
    import sys

    _INPUT = """\
5
10 3 5 2 3 6
10 3 5 1 1000000000 1000000000
139 2 139 1 1 1
139 1 1 1 1 1
139 7 10 3845 26982 30923

    """
    sys.stdin = io.StringIO(_INPUT)

    T = int(input())
    p = 0
    for i in range(T):
        n, a, b, x, y, z = map(int, input().split())
        y = min(y, a * x)
        z = min(z, b * x)

        if a / y > b / z:
            a, b = b, a
            y, z = z, y
        if n < a * a:
            print(min(y * i + (n - a * i) // b * z + (n - a * i) %
                b * x for i in range(n // a + 1)))
        else:
            print(min(z * i + (n - b * i) // a * y + (n - b * i) %
                a * x for i in range(a)))




main()
