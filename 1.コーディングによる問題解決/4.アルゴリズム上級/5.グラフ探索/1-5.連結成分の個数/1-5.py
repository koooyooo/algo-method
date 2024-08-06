import sys

sys.setrecursionlimit(10 ** 9)

N, M = [int(i) for i in input().split()]
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = [int(i) for i in input().split()]
    G[a].append(b)
    G[b].append(a)
seen = [False] * N


def dfs(n: int):
    seen[n] = True
    for ch in G[n]:
        if seen[ch]:
            continue
        dfs(ch)


count = 0
for n in range(N):
    if not seen[n]:
        count += 1
        dfs(n)


print(count)
