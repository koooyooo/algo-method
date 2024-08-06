import sys

sys.setrecursionlimit(10 ** 9)

N, X = [int(i) for i in input().split()]
As = [int(i) for i in input().split()]

G = [[] for _ in range(N)]
seen = [False] * N
depth = [-1] * N

for i, a in enumerate(As):
    G[a].append(i + 1)

depth[0] = 0


def dfs(n: int):
    seen[n] = True
    for ch in G[n]:
        if seen[ch]:
            continue
        depth[ch] = depth[n] + 1
        dfs(ch)


dfs(0)

print(depth[X])
