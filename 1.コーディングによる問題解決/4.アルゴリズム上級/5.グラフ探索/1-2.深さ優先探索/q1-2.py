N, M = [int(i) for i in input().split()]
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = [int(i) for i in input().split()]
    G[a].append(b)

for n in G:
    n.sort()

seen = [False] * N
seen[0] = True

order = []


def rec(n: int):
    seen[n] = True
    order.append(n)
    for ch in G[n]:
        if seen[ch]:
            continue
        rec(ch)


rec(0)

print(" ".join([str(i) for i in order]))
