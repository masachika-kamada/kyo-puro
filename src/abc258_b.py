def main():
#     import io
#     import sys

#     _INPUT = """\
# 4
# 1161
# 1119
# 7111
# 1811

#     """
#     sys.stdin = io.StringIO(_INPUT)

    n = int(input())
    A = [list(map(int, input())) for _ in range(n)]
    vals = []
    for i in range(n):
        for j in range(n):
            vals.append(get_all_direction(i, j, A, n))
    print(max(vals))


def get_all_direction(y, x, A, n):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    vals = []
    for dx, dy in directions:
        val = 0
        for i in range(n):
            val = val * 10 + A[(y + i * dy) % n][(x + i * dx) % n]
        vals.append(val)
    return max(vals)

main()
