def solve(s):
    _s = s.copy()
    _s[0], *_s[1:] = *_s[1:], _s[0]
    cnt = 1
    print("---while start", s)
    while _s != s:
        print(_s)
        _s[0], *_s[1:] = *_s[1:], _s[0]
        cnt += 1
    return cnt


def main():
    import io
    import sys

    _INPUT = """\
4 1
abac

    """
    sys.stdin = io.StringIO(_INPUT)

    n, k = map(int, input().split())
    s = list(input())
    cs = list(set(s))
    cnt = 1
    if n == 1:
        print(1)
    for i in range(n):
        for c in cs:
            print(s[i])
            if c == s[i]: 
                continue
            res = s.copy()
            print(res, c)
            print(res[i])
            res[i] = c
            cnt = min(cnt, solve(res))
    print(cnt)


main()
