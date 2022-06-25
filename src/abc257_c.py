def main():
#     import io
#     import sys

#     _INPUT = """\
# 5
# 10101
# 60 50 50 50 60

#     """
#     sys.stdin = io.StringIO(_INPUT)

    n = int(input())
    S = list(input())
    adult = []
    for i, s in enumerate(S):
        if s == "1":
            adult.append(i)
    w = list(map(int, input().split()))
    w_set = list(set(w))
    w_set.append(0)
    w_set.append(10 ** 10)
    dst = 0
    for w_i in w_set:
        ret = ret_acc(n, adult, w, w_i)
        # print(ret)
        dst = max(dst, ret)
    print(dst)


def ret_acc(n, a, w, thresh):
    dst = n - len(a)
    # print(a)
    # print(thresh, "dst", dst)
    for i, w_i in enumerate(w):
        if w_i >= thresh:
            if i in a:
                dst += 1
                # print("+1", i, w_i)
            else:
                dst -= 1
                # print("-1", i, w_i)
    return dst


main()
