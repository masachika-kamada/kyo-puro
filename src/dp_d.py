def main():
#     import io
#     import sys

#     _INPUT = """\
# 3 8
# 3 30
# 4 50
# 5 60

#     """
#     sys.stdin = io.StringIO(_INPUT)

    N, W = map(int, input().split())

    # DP 配列用意
    # i 番目までの品物を重さ j 以下で選ぶ場合、品物の総和の価値の最大値を dp[i][j] とする
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    # 漸化式にしたがって DP を実行する
    # i+1 番目の品物（重さ:w、価値:v）を選ぶのは
    # i 番目までの品物で重さ w を使って稼げる価値より i+1 番目の品物で稼げる価値 v のほうが大きい場合である
    for i in range(N):
        dp[i + 1] = dp[i].copy()  # 上書きを防ぐために .copy() は必須
        w, v = map(int, input().split())
        for j in range(W + 1 - w):
            dp[i + 1][j + w] = max(dp[i][j] + v, dp[i][j + w])
        # print(dp)

    # dp 配列の末尾が N 番目までの品物から重さ W 以下で選ぶ場合の品物の価値の最大値となる。
    # print(dp)
    print(dp[-1][-1])


main()
