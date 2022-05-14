def main():
    n = int(input())
    st = {}
    for i in range(n):
        s, t = input().split()
        if s not in st.keys():
            st[s] = [int(t), i + 1]
    vals = list(st.values())
    vals = sorted(vals, key=lambda x: (-x[0], x[1]))
    print(vals[0][1])


main()
