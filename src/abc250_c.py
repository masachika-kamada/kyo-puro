def main():
#     import io
#     import sys

#     _INPUT = """\
# 5 5
# 1
# 2
# 3
# 4
# 5

#     """
#     sys.stdin = io.StringIO(_INPUT)

    n, q = map(int, input().split())
    a = list(range(1, n + 1))
    b = list(range(0, n))
    d = dict(zip(a, b))
    # key: num, val: idx
    for i in range(q):
        num = int(input())
        """
        idx = a.index(num)とした部分がO(n)の計算量
        これが原因で時間内に終了しない
        indexを辞書に保存することで解決
        """
        # idx = a.index(num)
        idx = d[num]
        if idx == n - 1:
            # 値の変更
            a[idx], a[idx - 1] = a[idx - 1], a[idx]
            # indexの変更
            d[a[idx]], d[a[idx - 1]] = d[a[idx - 1]], d[a[idx]]
        else:
            # 値の変更
            a[idx], a[idx + 1] = a[idx + 1], a[idx]
            # indexの変更
            d[a[idx]], d[a[idx + 1]] = d[a[idx + 1]], d[a[idx]]
    print(*a)


main()
