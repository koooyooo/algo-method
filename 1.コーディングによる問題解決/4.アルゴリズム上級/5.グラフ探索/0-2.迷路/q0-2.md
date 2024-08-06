https://algo-method.com/tasks/424

## 行列からグラフへの変換
- 頂点番号が無いので(H,W)形式のTupleを使う
- Tuple値はListのIndexに使えないので 各種情報は辞書(Map)で取り扱う
- Graph構築時は、探索済みの左・上のセルを結合することを繰り返す

## 注意点
- `Ss`の様な二次元配列のIndexを`[h][w]`とすべきところを`[h,w]`とする誤り
- `append((h,w))`とすべきところを `append(h,w)`とする誤り
