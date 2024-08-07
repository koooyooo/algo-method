import sys

sys.setrecursionlimit(10 ** 9)

N = int(input())
Ps = [int(i) for i in input().split()]
G = [[] for _ in range(N)]
for i, p in enumerate(Ps):
    G[p].append(i+1)
seen = [False] * N
count = 0


def dfs(n: int):
    global count
    seen[n] = True
    if n != 0 and not G[n]:
        count += 1
    for ch in G[n]:
        if seen[ch]:
            continue
        dfs(ch)


dfs(0)

print(count)
