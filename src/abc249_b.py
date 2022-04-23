def main():
#     import io
#     import sys

#     _INPUT = """\
# AtCoder

#     """
#     sys.stdin = io.StringIO(_INPUT)
    # input = sys.stdin.readline

    s = input()
    if s.islower() == True:
        print("No")
        exit()
    elif s.isupper() == True:
        print("No")
        exit()
    a = list(s)
    # print(a)
    dst = list(set(a))
    # print(dst)
    if len(a) == len(dst):
        print("Yes")
    else:
        print("No")

main()
