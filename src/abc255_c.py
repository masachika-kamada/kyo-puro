def main():
#     import io
#     import sys

#     _INPUT = """\
# 10 20 -2 4

#     """
#     sys.stdin = io.StringIO(_INPUT)

    x, a, d, n = map(int, input().split())
    if n <= 2:
        arr = [a]
        for i in range(n - 1):
            arr.append(arr[-1] + d)
    if a < x:
        if d <= 0:  # 離れていく方向なので
            arr = [a]
        else:  # 近づいてくる方向
            skip = (x - a) // d
            skip = min(skip, n - 2)
            arr = [a + skip * d, a + skip * d + d]

    else:
        if d >= 0:  # 離れていく方向なので
            arr = [a]
        else:  # 近づいてくる方向
            skip = (x - a) // d
            skip = min(skip, n - 2)
            arr = [a + skip * d + d, a + skip * d]

    arr.sort()

    if x <= arr[0]:
        print(arr[0] - x)
    elif x >= arr[-1]:
        print(x - arr[-1])
    else:
        left = x - arr[0]
        right = arr[-1] - x
        print(min(left, right))


main()
