import sys

sys.setrecursionlimit(10 ** 9)

N = int(input())
G = [[] for _ in range(N)]
Ps = [int(i) for i in input().split()]
for i, p in enumerate(Ps):
    G[p].append(i + 1)
for n in G:
    n.sort()

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

str_order = [str(i) for i in order]
print(" ".join(str_order))
