def main():
    # import io
    # import sys

    # _INPUT = """\

    # """
    # sys.stdin = io.StringIO(_INPUT)
    # input = sys.stdin.readline

    n = int(input())
    h = list(map(int, input().split()))
    dp = [0] * (n + 1)
    for i in range(1, n):
        if i - 2 >= 0:
            dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]),
                        dp[i - 2] + abs(h[i] - h[i - 2]))
        else:
            dp[i] = dp[i - 1] + abs(h[i] - h[i - 1])
    print(dp[n - 1])


main()
