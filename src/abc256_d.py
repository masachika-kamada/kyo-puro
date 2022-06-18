def main():
    import io
    import sys

    _INPUT = """\
21
10 40
20 50
30 60
40 70
50 80
80 90
90 100
100 120
110 130
1000 2000
120 140
130 150
140 160
150 170
160 180
170 190
180 200
190 210
200 220
210 230
220 240

    """
    sys.stdin = io.StringIO(_INPUT)

    import bisect

    lrs = []
    n = int(input())
    for i in range(n):
        lr = list(map(int, input().split()))
        lrs.append(lr)
    lrs = sorted(lrs, key=lambda x: x[0])
    l = [x[0] for x in lrs]
    r = [x[1] for x in lrs]
    # print(lrs)
    start = 0
    while start < n:
        l_min = lrs[start][0]
        r_min = lrs[start][1]
        idx_pre = 0
        r_max = 0
        while True:
            idx = bisect.bisect_right(l, r_min)
            if idx_pre >= idx:
                # print(idx_pre)
                r_max = max(r_max, r[idx_pre - 1])
                break
            rs = r[idx_pre:idx]
            rs.append(r_max)
            print(idx_pre, idx)
            r_max = max(rs)
            r_min = r_max
            idx_pre = idx
            print("idx", idx)
            print("rs", rs)
        start = idx
        print(l_min, r_max)


main()
