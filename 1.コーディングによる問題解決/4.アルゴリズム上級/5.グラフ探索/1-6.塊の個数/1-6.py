import sys
from typing import Tuple

sys.setrecursionlimit(10 ** 9)

H, W = [int(i) for i in input().split()]
lines = []
for h in range(H):
    line = input()
    lines.append(line)

G = {}
seen = {}

for h in range(H):
    for w in range(W):
        if lines[h][w] != "#":
            continue
        # for simplicity to prevent easy mistakes
        current = (h,w)
        # init management vars
        G[current] = []
        seen[current] = False
        # creating graphs
        if h != 0 and lines[h-1][w] == "#":
            up = (h-1,w)
            G[current].append(up)
            G[up].append(current)
        if w != 0 and lines[h][w-1] == "#":
            left = (h,w-1)
            G[current].append(left)
            G[left].append(current)


# from python 3.9: `from typing import Tuple` isn't required, just using small case `tuple[int,int]` instead
def dfs(n: Tuple[int,int]):
    seen[n] = True
    for ch in G[n]:
        if seen[ch]:
            continue
        dfs(ch)


count = 0
for h in range(H):
    for w in range(W):
        if lines[h][w] == "#" and not seen[(h,w)]:
            count += 1
            dfs((h,w))

print(count)
