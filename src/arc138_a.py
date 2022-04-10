# https://atcoder.jp/contests/arc138/tasks/arc138_a

n, k = map(int, input().split())
a = list(map(int, input().split()))
a_idx = [[a[i], i] for i in range(n)]
a_idx = sorted(a_idx, key=lambda x: (x[0], -x[1]))

max_k_idx = -1
ans = 10**6

for val, j in a_idx:
    if j < k:
        max_k_idx = max(max_k_idx, j)
    elif max_k_idx != -1:
        ans = min(ans, j - max_k_idx)

if ans == 10**6:
    print(-1)
else:
    print(ans)
