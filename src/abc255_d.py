def main():
#     import io
#     import sys

#     _INPUT = """\
# 10 5
# 1000000000 314159265 271828182 141421356 161803398 0 777777777 255255255 536870912 998244353
# 555555555
# 321654987
# 1000000000
# 789456123
# 0

#     """
#     sys.stdin = io.StringIO(_INPUT)

    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    sum_A = sum(A)
    # 累積和を計算
    from itertools import accumulate
    accumulate_A = list(accumulate(A))

    import bisect
    for i in range(q):
        x = int(input())
        idx = bisect.bisect_left(A, x)
        if idx == 0:
            dst = sum_A - n * x
        elif idx == n:
            dst = n * x - sum_A
        else:
            dst = ((idx) * x - accumulate_A[idx - 1]) + ((sum_A - accumulate_A[idx - 1]) - (n - idx) * x)
        print(dst)


main()
