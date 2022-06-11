def solve(s, cnt):
    if "ARC" not in s:
        return s, cnt
    split = s.split("ARC")
    print(split)
    cnt += 1
    ress = []
    cnts = []
    if cnt % 2 == 0:
        for i in range(1, len(split)):
            res, cnt = solve("ARC".join(split[:i]) + "AC" + "ARC".join(split[i:]), cnt)
            ress.append(res)
            cnts.append(cnt)
            # print(res, cnt)
    else:
        for i in range(1, len(split)):
            res, cnt = solve("ARC".join(split[:i]) + "R" + "ARC".join(split[i:]), cnt)
            ress.append(res)
            cnts.append(cnt)
            # print(res, cnt)
    max_cnt = max(cnts)
    idx = cnts.index(max_cnt)
    print(ress, cnts)
    return ress[idx], max_cnt


def main():
    import io
    import sys

    _INPUT = """\
9
ARCARCARC

    """
    sys.stdin = io.StringIO(_INPUT)

    n = int(input())
    s = input()

    _, idx = solve(s, 0)
    print(idx)



main()
