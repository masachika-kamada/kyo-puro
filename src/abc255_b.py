def main():
    import io
    import sys

    _INPUT = """\

    """
    sys.stdin = io.StringIO(_INPUT)

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        x, y = map(int, input().split())


main()
