"""
TODO: 二分探索木
"""


def main():
    import io
    import sys

#     _INPUT = """\
# 31 415926 5
#     """
#     sys.stdin = io.StringIO(_INPUT)
    # input = sys.stdin.readline

    a, b, k = map(int, input().split())
    cnt = 0
    while a < b:
        cnt += 1
        a *= k
        # print(k, a)
    print(cnt)


main()
