https://algo-method.com/tasks/415

## 考え方
- 入力が複雑なのでグラフ化する
- 箱同士の容器と中身の関係は、有向グラフで表現する
- 箱は単一の箱にしか入らないため、グラフの経路は単一しかない
  - 深さの測定ではあるが、幅優先に限らず深さ優先でも探索可能


## ミス
- `dfs(0)` コール忘れ
- 開始番号の調整ミス
  - `enumerate` の indexの始点は `0`、箱番号では `1`

