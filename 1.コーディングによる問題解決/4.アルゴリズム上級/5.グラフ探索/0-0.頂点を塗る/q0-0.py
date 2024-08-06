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

depth_rev = [[] for _ in range(N)]
depth_rev[0].append(0)

q = deque()
q.append(0)

while q:
    n = q.popleft()
    for ch in G[n]:
        if seen[ch]:
            continue
        d = depth[n] + 1
        depth[ch] = d
        depth_rev[d].append(ch)
        seen[ch] = True
        q.append(ch)

for l in depth_rev:
    l.sort()

for i in range(max(depth) + 1):
    depth_rev_str = [str(d) for d in depth_rev[i]]
    print(" ".join(depth_rev_str))

