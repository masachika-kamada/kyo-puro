def main():
#     import io
#     import sys

#     _INPUT = """\
# 5 3 5
# 1 3 4
# 3 3 1 1 2

#     """
#     sys.stdin = io.StringIO(_INPUT)

    n, k, q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    for l in L:
        if A[l - 1] != n:
            if l < k and A[l] >= A[l - 1] + 2:
                A[l - 1] += 1
            elif l == k and A[l - 1] < n:
                A[l - 1] += 1
    print(*A)


main()
