import re

def is_valid(s):
    pattern = r'[A-Z][1-9][0-9]{5}[A-Z]'
    return re.match(pattern, s) is not None


def main():
#     import io
#     import sys

#     _INPUT = """\
# Q142857Z

#     """
#     sys.stdin = io.StringIO(_INPUT)

    s = input()
    # if len(s) == 8 and \
    #     "A" <= s[0] <= "Z" and \
    #     s[1:7].isdecimal() and \
    #     10 ** 5 <= int(s[1:7]) and \
    #     "A" <= s[-1] <= "Z":
    #     print("Yes")
    # else:
    #     print("No")

    if is_valid(s):
        print("Yes")
    else:
        print("No")


main()
