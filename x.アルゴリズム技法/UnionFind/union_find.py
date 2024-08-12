class UnionFind(object):

    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [1] * n
        self.siz = [1] * n

    def root(self, v) -> int:
        if self.par[v] == -1:
            return v
        self.par[v] = self.root(self.par[v])
        return self.par[v]

    def is_same(self, x, y) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x, y) -> bool:
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]
        return True

    def size(self, v):
        return self.siz[self.root(v)]
