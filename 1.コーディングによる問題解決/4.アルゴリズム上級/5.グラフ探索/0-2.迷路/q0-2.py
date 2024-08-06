from collections import deque


def read() -> list:
    return [int(i) for i in input().split()]


H, W = read()
X0, Y0, X1, Y1 = read()
Ss = []
for _ in range(H):
    Ss.append(input())

# グラフ等作成
G = {}
seen = {}
depth = {}
for h in range(H):
    for w in range(W):
        current = (h,w)

        # Map要素初期化
        G[current] = []
        seen[current] = False
        depth[current] = -1

        # 探索済みの左部分、上部分をグラフに追加
        if Ss[h][w] != 'W':
            continue
        if w != 0 and Ss[h][w-1] == 'W':
            left = (h,w-1)
            G[current].append(left)
            G[left].append(current)
        if h != 0 and Ss[h-1][w] == 'W':
            up = (h-1, w)
            G[current].append(up)
            G[up].append(current)


seen[(X0,Y0)] = True
depth[(X0,Y0)] = 0

q = deque()
q.append((X0,Y0))

while q:
    n = q.popleft()
    for ch in G[n]:
        if seen[ch]:
            continue
        seen[ch] = True
        depth[ch] = depth[n] + 1
        q.append(ch)

print(depth[(X1,Y1)])
