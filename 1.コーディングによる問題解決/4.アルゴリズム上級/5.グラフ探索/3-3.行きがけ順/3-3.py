import sys

sys.setrecursionlimit(10 ** 9)

N = int(input())
As = [int(i) for i in input().split()]
G = [[] for _ in range(N)]
for i, a in enumerate(As):
    G[a].append(i+1)
for n in range(N):
    G[n].sort()
seen = [False] * N
order = []


def dfs(n: int):
    seen[n] = True
    order.append(n)
    for ch in G[n]:
        if seen[ch]:
            continue
        dfs(ch)

dfs(0)

st_order = [str(i) for i in order]
print(" ".join(st_order))
