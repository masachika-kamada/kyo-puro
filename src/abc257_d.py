def main():
    import io
    import sys

    _INPUT = """\

    """
    sys.stdin = io.StringIO(_INPUT)

    n = int(input())
    for _ in range(n):
        x, y, p = map(int, input().split())



main()
