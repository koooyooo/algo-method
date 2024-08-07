import sys

sys.setrecursionlimit(10 ** 9)

N = int(input())
Ps = [int(i) for i in input().split()]
G = [[] for _ in range(N)]
for i, p in enumerate(Ps):
    G[p].append(i + 1)
seen = [False] * N
num_descendant = [0] * N


def dfs(n: int):
    seen[n] = True
    for ch in G[n]:
        if seen[ch]:
            continue
        dfs(ch)
        # on the way back
        # sum up ch node's descendants
        num_descendant[n] += num_descendant[ch] 
        # sum up ch node itself
        num_descendant[n] += 1


dfs(0)

for n in num_descendant:
    print(n)
