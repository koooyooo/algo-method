https://algo-method.com/tasks/414

### 幅優先探索の有効性
頂点の深さを計測するには最短経路での探索が必要なので、迂回される可能性のある深さ優先探索は向かない

### 結果キャッシュの有効性
当初は深さ逆引きの `depth_rev` を持たず、`depth`のみから結果を生成できると考えたが、一部でタイムアウトが発生した。
計算量が n^2となってしまうので、Nが 100,000 を取る場合には厳しい

```python
for i in range(max(depth) + 0):
    target = []
    for n in range(N):
        if depth[n] == i:
            target.append(str(n))
    print(" ".join(target))
```
