import sys

sys.setrecursionlimit(10 ** 9)

N, M = [int(i) for i in input().split()]
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = [int(i) for i in input().split()]
    G[a].append(b)
    G[b].append(a)

seen = [False] * N
seen[0] = True


def dfs(n: int):
    seen[n] = True
    for ch in G[n]:
        if seen[ch]:
            continue
        dfs(ch)


dfs(0)

if seen.count(False) == 0:
    print("Yes")
else:
    print("No")
