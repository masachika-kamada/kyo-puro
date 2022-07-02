def main():
    import io
    import sys

    _INPUT = """\
4
1161
1119
7111
1811

    """
    sys.stdin = io.StringIO(_INPUT)

    n = int(input())
    A = []
    for _ in range(n):
        A.append(list(map(int, list(input()))))
    print(A)
    print(get_all_direction(1, 3, A, n))


def get_all_direction(y, x, A, n):
    dst_w = ""
    dst_a = ""
    dst_s = ""
    dst_d = ""
    dst_wa = ""
    dst_as = ""
    dst_sd = ""
    dst_dw = ""
    for i in range(n):
        x_p_i = x + i
        if x_p_i >= n:
            x_p_i -= n
        y_p_i = y + i
        if y_p_i >= n:
            y_p_i -= n
        dst_d += str(A[y][x_p_i])
        dst_a += str(A[y][x - i])
        dst_w += str(A[y - i][x])
        dst_s += str(A[y_p_i][x])
        dst_wa += str(A[y - i][x - i])
        dst_as += str(A[y_p_i][x - i])
        dst_sd += str(A[y_p_i][x_p_i])
        dst_dw += str(A[y - i][x_p_i])
    dst = [dst_d, dst_a, dst_w, dst_s, dst_wa, dst_as, dst_sd, dst_dw]
    print(dst)
    for i in range(len(dst)):
        dst[i] = int(dst[i])
    return max(dst)

main()
