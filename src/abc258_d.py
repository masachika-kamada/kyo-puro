def main():
#     import io
#     import sys

#     _INPUT = """\
# 10 1000000000
# 3 3
# 1 6
# 4 7
# 1 8
# 5 7
# 9 9
# 2 4
# 6 4
# 5 1
# 3 1

#     """
#     sys.stdin = io.StringIO(_INPUT)

    n, x = map(int, input().split())
    a, b = map(int, input().split())
    A = [a]
    B = [b]
    minB = {0: b}
    tmp = b
    for i in range(1, n):
        a, b = map(int, input().split())
        A.append(a + A[-1])
        B.append(b + B[-1])
        if b < tmp:
            minB[i] = b
            tmp = b

    dst = 10 ** 20
    for key in minB:
        if key > x - 1:
            break
        # print(key, minB[key])
        dst = min(dst, A[key] + B[key] + (x - key - 1) * minB[key])
        # print(dst, A[key] + B[key] + (x - key - 1) * minB[key])
    print(dst)


main()
