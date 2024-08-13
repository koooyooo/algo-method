# Union Find
Union Find は頂点の集合を元に、集合の統合や同一判定を行うもの。

## Attributes
- `par` 各頂点の親頂点
- `rank` 各頂点を含む木の高さ
- `siz` 各頂点を含む木のサイズ（頂点数）

## Methods

### `__init__`
各属性の初期化を行う。 未知の親は `-1`、高さとサイズは`1`。
```python
def __init__(self, n):
    self.par = [-1] * n
    self.rank = [1] * n
    self.siz = [1] * n
```

### `root`
指定の頂点の根を返す。

- 自身が頂点なら自身を返す
- それ以外は再帰的に親を探す

再帰的な探索の過程で、中間要素の親は全て rootとなってしまう。
これは真実とは異なるデータとなるが、ユースケース上での不都合は生じず、むしろ計算上の短縮経路となる。
```python
def root(self, v) -> int:
    if self.par[v] == -1:
        return v
    self.par[v] = self.root(self.par[v])
    return self.par[v]
```

### `is_same`
2つの頂点が、同じ根付き木に属しているかを返す。これは両者が同じ `root`を共有しているかで判定可能である。
```python
def is_same(self, x, y) -> bool:
    return self.root(x) == self.root(y)
```

### `unite`
2つの頂点が属する根付き木を統合する。
- 両者の根を取得する
- 高い木に低い木を接ぎ木する（Xを高い方と仮定する）
  - **Xの高さ** >= **Yの高さ** でなければ両者を Swapする
  - 親を入れ替える（`rx`の直下に`ry`を接ぎ木）
  - 高さを入れ替える
    - **Xの高さ** == **Yの高さ** の場合、根本に接ぎ木した分、全体の高さを `+1`
    - それ以外は元々の **Xの高さ** に吸収されるため変更なし
  - `rx`のサイズには `ry`の分を追加する

```python
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
```

**全体像**
```python
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

```