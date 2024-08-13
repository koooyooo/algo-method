Max = 10 ** 5


class Node:
    def __init__(self):
        self.length = Max
        self.fixed = False


def run(N: int, edges: list, start: int, end: int, idx_from_1: bool) -> int:
    G = {}
    Ns = {}
    #
    for n in range(N):
        if idx_from_1:
            n = n + 1
        G[n] = []
        Ns[n] = Node()
    weight = {}
    for e in edges:
        f = e[0]
        t = e[1]
        w = e[2]
        G[f].append(t)
        G[t].append(f)
        weight[(f, t)] = w
        weight[(t, f)] = w

    Ns[start].length = 0
    Ns[start].fixed = True

    tail = start

    while tail != end:
        loosen_ch = []
        # 子頂点を緩和
        for ch in G[tail]:
            if Ns[ch].fixed:
                continue
            if Ns[ch].length < Ns[tail].length + weight[(tail, ch)]:
                continue
            Ns[ch].length = Ns[tail].length + weight[(tail, ch)]
            loosen_ch.append(ch)
        shortest_ch = -1
        shortest_len = Max
        for n in loosen_ch:
            if Ns[n].length < shortest_len:
                shortest_ch = n
                shortest_len = Ns[n].length
        Ns[shortest_ch].fixed = True
        tail = shortest_ch

    return Ns[tail].length

# 1 2 3 6 5 のコースを進んでいる
# 緩和できたかではなく、最短かを条件に判定すべき