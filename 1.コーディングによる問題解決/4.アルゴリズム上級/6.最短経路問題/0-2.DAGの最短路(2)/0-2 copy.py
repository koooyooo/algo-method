MAX = 10 ** 7

class Edge(object):
    def __init__(self, f, t, l):
        self.frm = f
        self.to = t
        self.length = l


N, M = [int(i) for i in input().split()]
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = [int(i) for i in input().split()]
    G[u].append(Edge(u, v, w))

distance = [MAX] * N
distance[0] = 0


def dfs(n: int):
    for edge in G[n]:
        dist_candidate = distance[n] + edge.distance
        if distance[edge.to] <= dist_candidate:
            continue
        distance[edge.to] = dist_candidate 
        dfs(edge.to)


dfs(0)

if distance[N-1] == MAX:
    print(-1)
else:
    print(distance[N-1])
