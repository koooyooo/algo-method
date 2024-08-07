import sys

sys.setrecursionlimit(10 ** 9)

N = int(input())
Ps = [int(i) for i in input().split()]
G = [[] for _ in range(N)]
for i, p in enumerate(Ps):
    G[p].append(i + 1)
seen = [False] * N
depth = [-1] * N
depth[0] = 0


def dfs(n: int):
    seen[n] = True
    for ch in G[n]:
        if seen[ch]:
            continue
        depth[ch] = depth[n] + 1
        dfs(ch)


dfs(0)

# 2-2.py を元に以下の結果集計部分だけ変更
print(max(depth))
