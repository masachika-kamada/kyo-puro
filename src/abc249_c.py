def main():
    import io
    import sys

    _INPUT = """\
4 2
abi
aef
bc
acg

    """
    sys.stdin = io.StringIO(_INPUT)

    # n, k = map(int, input().split())
    # s = []
    # for i in range(n):
    #     s.append(input())
    # a = list("".join(s))
    # a = list(set(a))

    # cnt = 0
    # for i in range(n + 1):
    #     comb = itertools.combinations(s, i)
    #     for c in comb:
    #         c = "".join(c)
    #         count = 0
    #         for ch in a:
    #             if c.count(ch) == k:
    #                 count += 1
    #         if count > cnt:
    #             cnt = count

    # print(cnt)

    from collections import defaultdict

    N, K = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    n2 = 1 << N
    # print(n2)
    for t in range(n2):
        d = defaultdict()
        for i in range(N):
            if t & (0x01 << i) != 0x00:
                for s in S[i]:
                    if s in d:
                        d[s] += 1
                    else:
                        d[s] = 1
        cnt = 0
        for k, v in d.items():
            if v == K:
                cnt += 1
        ans = max(ans, cnt)

    print(ans)


main()
