from collections import deque

N, M = [int(i) for i in input().split()]
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = [int(i) for i in input().split()]
    G[a].append(b)
    G[b].append(a)

seen = [False] * N
seen[0] = True

depth = [-1] * N
depth[0] = 0

q = deque()
q.append(0)

while q:
    n = q.popleft()
    for ch in G[n]:
        if seen[ch]:
            continue
        seen[ch] = True
        depth[ch] = depth[n] + 1
        q.append(ch)

print(max(depth))
