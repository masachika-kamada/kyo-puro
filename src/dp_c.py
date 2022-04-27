def main():
#     import io
#     import sys

#     _INPUT = """\
# 3
# 10 40 70
# 20 50 80
# 30 60 90

#     """
#     sys.stdin = io.StringIO(_INPUT)

    n = int(input())
    s = [list(map(int, input().split())) for i in range(n)]
    dp = [[0] * 3 for _ in range(n)]
    for i in range(n):
        for j in range(3):
            if i == 0:
                dp[i][j] = s[i][j]
            else:
                c = return_other(j)
                dp[i][j] = max(dp[i - 1][c[0]], dp[i - 1][c[1]]) + s[i][j]
    print(max(dp[-1]))


def return_other(j):
    a = list(range(3))
    a.remove(j)
    return a


main()
