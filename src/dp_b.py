"""
・動的計画法：求めたい問題に対して部分的な解を順に求め
その解を利用しながら本来求めたい解を導き出す手法
・疑似コード
dp = 問題に応じた初期値で初期化された配列(0や考えられる最大値+1など)
dp = 初期条件

解を求めるまで繰り返す
  dp = dpテーブルの解を利用して解を求める
"""


def main():
#     import io
#     import sys

#     _INPUT = """\
# 5 3
# 10 30 40 50 20

#     """
#     sys.stdin = io.StringIO(_INPUT)
    # input = sys.stdin.readline

    n, k = map(int, input().split())
    h = list(map(int, input().split()))

    # 初期化
    dp = [10**5 + 1] * n

    # 初期条件
    # kの値が変わっても初期条件は0, 1
    dp[0] = 0
    dp[1] = abs(h[1] - h[0])

    for i in range(2, n):
        sum_cost = []
        for j in range(1, k + 1):
            if i - j < 0:
                break
            sum_cost.append(abs(h[i] - h[i - j]) + dp[i - j])
        dp[i] = min(sum_cost)

    print(dp[-1])


main()
