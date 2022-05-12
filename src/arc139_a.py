def main():
#     import io
#     import sys

#     _INPUT = """\
# 8
# 2 0 2 2 0 4 2 4

#     """
#     sys.stdin = io.StringIO(_INPUT)

    N = int(input())
    T = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        plus = 2 ** T[i] - ans % (2 ** T[i])
        ans += plus
        if ans % (2 ** (T[i] + 1)) == 0:  # 指定の桁数よりも0が続いた場合
            ans += 2 ** T[i]
    print(ans)


main()
