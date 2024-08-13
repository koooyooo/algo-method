Max = 10 ** 5


class Node:
    def __init__(self):
        self.distance = Max
        self.fixed = False


def run(N: int, edges: list, start: int, end: int, idx_from_1: bool) -> int:
    G = {}
    Ns = {}
    for n in range(N):
        if idx_from_1:
            n = n + 1
        G[n] = []
        Ns[n] = Node()
    edge_dist = {}
    for e in edges:
        f = e[0]
        t = e[1]
        w = e[2]
        G[f].append(t)
        G[t].append(f)
        edge_dist[(f, t)] = w
        edge_dist[(t, f)] = w

    Ns[start].distance = 0
    Ns[start].fixed = True
    # 最小コストの終点
    shortest_tail = start

    while shortest_tail != end:
        shortest_ch = -1
        shortest_dist = Max
        # 子頂点から最短のものを検索し、次回の始点とする
        for ch in G[shortest_tail]:
            if Ns[ch].fixed:
                continue
            # 緩和できたか否かに関わらず、最短の子要素を選択
            if Ns[shortest_tail].distance + edge_dist[(shortest_tail, ch)] < Ns[ch].distance:
                Ns[ch].distance = Ns[shortest_tail].distance + edge_dist[(shortest_tail, ch)]
            if Ns[ch].distance < shortest_dist:
                shortest_ch = ch
                shortest_dist = Ns[ch].distance
        Ns[shortest_ch].fixed = True
        shortest_tail = shortest_ch

    return Ns[shortest_tail].distance
