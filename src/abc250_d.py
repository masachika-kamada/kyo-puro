def prime(n):  # エラトステネスのふるい
    candidate = list(range(2, n + 1))  # 候補
    prime = []
    limit = n**0.5 + 1  # +1がないと平方数を素数にしてしまう

    while True:
        p = candidate[0]
        if limit <= p:
            prime.extend(candidate)  # この時点での残っているのは素数
            break
        prime.append(p)  # pを素数リストに登録

        candidate = [i for i in candidate if i % p != 0]
    return prime


def main():
    import io
    import sys
    import bisect

    _INPUT = """\
250

    """
    sys.stdin = io.StringIO(_INPUT)

    n = int(input())
    cnt = 0
    if n <= 1:
        print(0)
        exit()
    u = int((n / 2) ** (1 / 3))
    sosu = prime(u)
    ps = prime((int(n ** 0.25)) // 1)
    for p in ps:
        qs = int((n / p) ** (1 / 3) // 1)
        index = bisect.bisect_left(sosu, qs)
        print(p, qs, index)
        cnt += index + 1
    print(sosu)
    print(cnt)


main()
