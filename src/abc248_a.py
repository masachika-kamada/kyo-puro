def main():
    import io
    import sys

#     _INPUT = """\
# 023456789

#     """
    # sys.stdin = io.StringIO(_INPUT)
    # input = sys.stdin.readline

    s = input()
    # print(s)

    nums = list(range(10))
    # print(nums)
    for i in range(9):
        # print(int(s[i]))
        nums.remove(int(s[i]))
    print(nums[0])


main()
