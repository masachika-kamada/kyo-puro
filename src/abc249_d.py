def main():
#     import io
#     import sys

#     _INPUT = """\
# 10
# 1 3 2 4 6 8 2 2 3 7

#     """
#     sys.stdin = io.StringIO(_INPUT)

    from collections import Counter
    N = int(input())
    A = list(map(int, input().split()))
    c = Counter(A)
    max_a = max(A)
    ans = 0
    for i in range(1, max_a + 1):
        # jをiで割り切れることが条件
        # 増分をiにすれば必ず割り切れる
        for j in range(i, max_a + 1, i):
            # それぞれのkeyに紐づいたvalをかける
            # e.g. 2 2 2 1
            # --> 2 / 1 = 2で(2, 1, 2)の組を考えるとき
            # 整数の組の候補は3*1*3=9個となる
            ans += c[j] * c[i] * c[j // i]
    print(ans)


main()
