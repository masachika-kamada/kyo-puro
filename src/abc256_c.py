def main():
    # import io
    # import sys

    # _INPUT = """\

    # """
    # sys.stdin = io.StringIO(_INPUT)

    A = list(map(int, input().split()))
    h = A[:3]
    w = A[3:]

    ans = 0
    for i in range(1, 31):
        for j in range(1, 31):
            for k in range(1, 31):
                for l in range(1, 31):
                    a = h[0] - i - j
                    b = h[1] - k - l
                    c = w[0] - i - k
                    d = w[1] - j - l
                    e = w[2] - a - b
                    if min(a, b, c, d, e) > 0 and h[2] == c + d + e:
                        ans += 1
    print(ans)


main()

# i | j | a
# --+---+---
# k | l | b
# --+---+---
# c | d | e
