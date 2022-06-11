def main():
    import io
    import sys

    _INPUT = """\
10 5
1000000000 314159265 271828182 141421356 161803398 0 777777777 255255255 536870912 998244353
555555555
321654987
1000000000
789456123
0

    """
    sys.stdin = io.StringIO(_INPUT)

    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    sum_A = sum(A)
    a_min = A[0]
    a_lower_sum = sum_A - A[0] * n
    a_max = A[-1]
    a_upper_sum = A[-1] * n - sum_A
    a_center = A[n // 2]
    ac_lower = A[:n // 2]
    ac_upper = A[n // 2:]
    ac_lower_sum = ac_lower[-1] * len(ac_lower) - sum(ac_lower)
    ac_upper_sum = sum(ac_upper) - ac_upper[0] * len(ac_upper)

    for i in range(q):
        x = int(input())
        if x < a_min:
            dst = a_lower_sum + (a_min - x) * n
        elif x > a_max:
            dst = a_upper_sum + (x - a_max) * n
        elif x < a_center:
            dst = ac_lower_sum + (a_center - x) * len(ac_lower)
            for a in ac_upper:
                dst += abs(a - x)
        else:
            dst = ac_upper_sum + (x - a_center) * len(ac_upper)
            for a in ac_lower:
                dst += abs(a - x)
        print(dst)


main()
