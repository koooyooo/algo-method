N = int(input())
G = [[] for _ in range(N)]
parent = [-1] * N
for _ in range(N-1):
    a, b = [int(i) for i in input().split()]
    G[a].append(b)
    parent[b] = a
for n in range(N):
    G[n].sort()
Q = int(input())
Vs = []
for _ in range(Q):
    v = int(input())
    Vs.append(v)


for v in Vs:
    p = parent[v]
    bors = G[p]
    st_bros = [str(i) for i in bors]
    print(" ".join(st_bros))
