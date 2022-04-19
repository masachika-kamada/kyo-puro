def main():
#     import io
#     import sys

#     _INPUT = """\
# 0 0 23 59

#     """
#     sys.stdin = io.StringIO(_INPUT)
    # input = sys.stdin.readline

    a, b, c, d = map(int, input().split())
    if a < c:
        print("Takahashi")
    elif a > c:
        print("Aoki")
    else:
        if b <= d:
            print("Takahashi")
        else:
            print("Aoki")


main()
