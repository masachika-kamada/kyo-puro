def main():
    # import io
    # import sys

    # _INPUT = """\

    # """
    # sys.stdin = io.StringIO(_INPUT)

    k = int(input())  # 0 <= k <= 100
    h = 21 + k // 60
    m = k % 60
    print(f"{h:02}:{m:02}")


main()
