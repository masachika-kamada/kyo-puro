def get_prime(n):
    if n < 2:
        return []
    candidate = list(range(n + 1))
    candidate[1] = 0
    for i in candidate:
        if i > 1:
            for j in range(i + i, len(candidate), i):
                candidate[j] = 0
    prime = [x for x in candidate if x != 0]
    return prime


def main():
    import bisect

    n = int(input())
    cnt = 0
    # qを得るための素数テーブル
    sosu = get_prime(round((n / 2) ** (1 / 3)))
    if len(sosu) <= 1:
        print(0)
        exit()
    # pの候補となる素数テーブル
    ps = get_prime(round(n ** 0.25))
    for p in ps:
        # pから計算される天井を求める
        # 計算誤差で過小評価されることがある
        # 一度大きめに取って条件式で補正
        q = (n / p) ** (1 / 3) + 1
        idx_q = bisect.bisect_right(sosu, q) - 1
        idx_p = bisect.bisect_right(sosu, p) - 1
        while sosu[idx_p] * (sosu[idx_q] ** 3) > n:
            idx_q -= 1
        if sosu[idx_p] < sosu[idx_q]:
            cnt += idx_q - idx_p
    print(cnt)


main()
