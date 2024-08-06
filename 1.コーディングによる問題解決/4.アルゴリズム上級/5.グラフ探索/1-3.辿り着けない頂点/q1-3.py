import sys

sys.setrecursionlimit(10 ** 9)

N, M = [int(i) for i in input().split()]
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = [int(i) for i in input().split()]
    G[a].append(b)

seen = [False] * N


def dfs(n: int):
    seen[n] = True
    for ch in G[n]:
        if seen[ch]:
            continue
        dfs(ch)


dfs(0)

print(seen.count(False))
