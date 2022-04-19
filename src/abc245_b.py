def main():
    # import io
    # import sys

    # _INPUT = """\

    # """
    # sys.stdin = io.StringIO(_INPUT)
    # input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    all_nums = list(range(2001))
    a = list(set(a))

    for i in a:
        all_nums.remove(i)
    print(min(all_nums))


main()
