"""
bisect.bisect_left(a, x, lo=0, h=len(a))

引数は以下になります(他の関数においても同様)
a: ソート済みリスト
x: 挿入したい値
lo: 探索範囲の下限
hi: 探索範囲の上限
(lo, hiはスライスと同様の指定方法)

bisect_leftはソートされたリストaに対して順序を保ったままxを挿入できる箇所を探索します
"""


def main():
    import io
    import sys
    import bisect

    _INPUT = """\
    4
    1 2 3
    2 2
    1 3 4
    2 3

    """
    sys.stdin = io.StringIO(_INPUT)

    # input = sy s.stdin.readline
    Q = int(input())
    X = [0]  # ボールに書かれた数
    N = [0]  # ボールの数
    S = [0]  # XとNの掛け算
    Nr = 0
    Sr = 0
    for _ in range(Q):
        P = list(map(int, input().split()))
        if P[0] == 1:
            X.append(P[1])
            N.append(N[-1] + P[2])
            S.append(S[-1] + P[1] * P[2])
        else:
            x = bisect.bisect_left(N, Nr + P[1])  # 今までのボールの合計数でsearchsorted
            print(x, S, P, X)
            print(S[x - 1] + (P[1] + Nr - N[x - 1]) * X[x] - Sr)
            Nr, Sr = Nr + P[1], S[x - 1] + (P[1] + Nr - N[x - 1]) * X[x]


main()
