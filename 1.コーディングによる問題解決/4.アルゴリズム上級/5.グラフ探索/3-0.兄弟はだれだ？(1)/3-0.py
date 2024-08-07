N = int(input())
Ps = [int(i) for i in input().split()]
G = [[] for _ in range(N)]
for i, p in enumerate(Ps):
    G[p].append(i+1)
for n in range(N):
    G[n].sort()

Q = int(input())
Vs = []
for _ in range(Q):
    Vs.append(int(input()))

for v in Vs:
    p = Ps[v-1]
    bros = G[p]
    st_bros = [str(i) for i in bros]
    print(" ".join(st_bros))
