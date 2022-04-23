def main():
#     import io
#     import sys

#     _INPUT = """\
# 1 1 1 1 1 1 1

#     """
#     sys.stdin = io.StringIO(_INPUT)
    # input = sys.stdin.readline

    a, b, c, d, e, f, x = map(int, input().split())
    taka = a + c
    taka_res = (x // taka) * (a * b)
    if (x % taka) >= a:
        taka_res += a * b
    else:
        taka_res += (x % taka) * b
    aoki = d + f
    aoki_res = (x // aoki) * (d * e)
    if (x % aoki) >= d:
        aoki_res += d * e
    else:
        aoki_res += (x % aoki) * e

    if taka_res > aoki_res:
        print("Takahashi")
    elif taka_res == aoki_res:
        print("Draw")
    else:
        print("Aoki")



main()
