# setへのcastを多用すると計算時間がかさむ

def main():
    import itertools

    n, w = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    a = [i for i in a if i <= w]
    good_nums = a.copy()

    for i in range(1, min(n, 3)):
        comb = itertools.combinations(a, i + 1)
        comb = [sum(i) for i in comb if sum(i) <= w]
        good_nums.extend(comb)

    print(len(set(good_nums)))


main()
