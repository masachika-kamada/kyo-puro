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
    import io
    import sys

    _INPUT = """\
3 8
3 30
4 50
5 60

    """
    sys.stdin = io.StringIO(_INPUT)
    input = sys.stdin.readline

    import math

    N, W = map(int, input().split())

    # dp 配列の用意
    # i 番目までの品物から価値 j で選べる品物の重さの総和の最小値を dp[i][j] とする
    # 品物の価値の総和の最大値を L とする。
    # 今回は価値 1000 の品物が 100 個用意される可能性を考えて L = 100000 とする
    # 重さの最小値に無限大を入れて初期化する
    L = 100000
    dp = [[math.inf] * (L + 1) for _ in range(N + 1)]

    # 初期条件を入れる
    dp[0][0] = 0

    # 漸化式にしたがって DP を実行する
    # ここでは重さの最小値が小さくなるように品物を選ぶ
    for i in range(N):
        w, v = map(int, input().split())
        for j in range(L + 1):
            # i+1 番目の品物 （重さ:w、価値:v）が選ばれるのは
            # i 番目までの品物で価値 v を節約して減らせる重さが w 以下のとき
            if j - v >= 0:
                dp[i + 1][j] = min(dp[i][j], dp[i][j - v] + w)
            else:
                dp[i + 1][j] = dp[i][j]

    print(dp[N][30:60])

    # dp[N][j] を先頭から調べたとき、最後に W 以下になる j を答えとする
    for i, d in enumerate(dp[N]):
        if d <= W:
            maxv = i
            print(i)
    print(maxv)


main()
