"""
考慮漏れ: s_i == t_i
自分の姓と名が同じであろうが他と違えばあだ名が付けられる
考えるべきは他人と姓と名両方被るのか
"""


def main():
    import io
    import sys

    # _INPUT = """\
    # 3
    # taro taro
    # tanaka jiro
    # suzuki hanako

    # """
    # sys.stdin = io.StringIO(_INPUT)
    input = sys.stdin.readline

    n = int(input())
    s, t = [], []
    for i in range(n):
        u, v = input().split()
        s.append(u)
        t.append(v)

    for i in range(n):
        flag_s, flag_t = False, False
        for j in range(n):
            if i == j:
                continue
            if s[i] == s[j] or s[i] == t[j]:
                flag_s = True
            if t[i] == s[j] or t[i] == t[j]:
                flag_t = True
            if flag_s and flag_t:
                print("No")
                exit()
    print("Yes")


main()
