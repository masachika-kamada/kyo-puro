def main():
#     import io
#     import sys

#     _INPUT = """\
# 2 1
# 2
# -100000 -100000
# 100000 100000

#     """
#     sys.stdin = io.StringIO(_INPUT)

    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    X = []
    Y = []
    for i in range(n):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    # それぞれの明かりのない座標から最も近い明かりまでの距離を求める
    # その距離の中で最長のものを出力する
    distance = []
    for i in range(n):
        if i + 1 in A:
            continue
        d_nearest = 10 ** 15
        for a in A:
            d = (X[i] - X[a - 1]) ** 2 + (Y[i] - Y[a - 1]) ** 2
            if d < d_nearest:
                d_nearest = d
        distance.append(d_nearest)
    print(max(distance) ** 0.5)


main()
