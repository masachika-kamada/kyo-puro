def main():
    import io
    import sys

#     _INPUT = """\
# 5
# 3 1 4 1 5
# 4
# 1 5 1
# 2 4 3
# 1 5 2
# 1 3 3

#     """
#     sys.stdin = io.StringIO(_INPUT)
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        l, r, x = map(int, input().split())
        num = sorted(a[l - 1:r - 1])
        try:
            idx = num.index(x)
            cnt = idx + 1
            # print("cnt,", cnt)
            if cnt == r - l:
                print(1)
                continue
            while num[cnt] == x:
                cnt += 1
            print(cnt - idx)
        except:
            print(0)


main()
