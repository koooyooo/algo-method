from collections import deque

H, W = [int(i) for i in input().split()]
X0, Y0, X1, Y1 = [int(i) for i in input().split()]

# create lines
lines = []
for h in range(H):
    line = input()
    lines.append(line)

# global vars
G = {}
seen = {}
distance = {}

# create graph
for h in range(H):
    for w in range(W):
        if lines[h][w] != "W":
            continue
        current = (h,w)
        # init global vars 
        G[current] = []
        distance[current] = -1
        seen[current] = False
        # set up graph content
        if h != 0 and lines[h-1][w] == "W":
            up = (h-1,w)
            G[current].append(up)
            G[up].append(current)
        if w != 0 and lines[h][w-1] == "W":
            left = (h,w-1)
            G[current].append(left)
            G[left].append(current)


start = (X0,Y0)
seen[start] = True
distance[start] = 0

q = deque()
q.append(start)

while q:
    n = q.popleft()
    for ch in G[n]:
        if seen[ch]:
            continue
        seen[ch] = True
        distance[ch] = distance[n] + 1
        q.append(ch)

end = (X1,Y1)
print(distance[end])
