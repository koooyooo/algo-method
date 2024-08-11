MAX = 10 ** 7

To = 0
Len = 1

N, M = [int(i) for i in input().split()]
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = [int(i) for i in input().split()]
    G[u].append((v, w))

distance = [MAX] * N
distance[0] = 0


def dfs(n: int):
    for edge in G[n]:
        dist_candidate = distance[n] + edge[Len]
        if distance[edge[To]] <= dist_candidate:
            continue
        distance[edge[To]] = dist_candidate 
        dfs(edge[To])


dfs(0)

if distance[N-1] == MAX:
    print(-1)
else:
    print(distance[N-1])
