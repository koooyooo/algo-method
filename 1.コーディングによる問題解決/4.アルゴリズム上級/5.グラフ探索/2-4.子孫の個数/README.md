https://algo-method.com/tasks/434

## 考え方
- 子孫の個数は行きがけには不明なので帰りがけに集計する
- 帰りがけの管理には、スタック内で情報を管理し続ける深さ優先探索が最適
- 子孫数を管理する `num_descendant` 配列を用意し、帰りがけに子の `num_descendant` を親に加算する

