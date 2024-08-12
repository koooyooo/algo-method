import unittest
from union_find import UnionFind


class TestUnionFind(unittest.TestCase):

    def setUp(self):
        # 0 - 1 - 3
        #       - 4
        #   - 2 - 5
        #       - 6
        self.tree1 = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]

        # 7 - 8
        #   - 9 - 10
        self.tree2 = [[7, 8], [7, 9], [9, 10]]

        self.uf = UnionFind(14)
        for f, t in self.tree1:
            self.uf.unite(f, t)
        for f, t in self.tree2:
            self.uf.unite(f, t)

    # 統合後にサイズが整っていること
    def test_united_size(self):
        self.assertEqual(7, self.uf.size(0))
        self.assertEqual(4, self.uf.size(7))
        # 統合
        self.uf.unite(0, 7)
        self.assertEqual(11, self.uf.size(0))
        self.assertEqual(11, self.uf.size(7))

    def test_united_root(self):
        self.assertEqual(0, self.uf.root(0))
        # self.assertEqual(7, self.uf.root(7))
        # # 統合
        # self.uf.unite(0, 7)
        # self.assertEqual(0, self.uf.root(0))
        # self.assertEqual(0, self.uf.root(7))

    def test_united_is_same(self):
        self.assertEqual(False, self.uf.is_same(0, 7))
        # 統合
        self.uf.unite(0, 7)
        self.assertEqual(True, self.uf.is_same(0, 7))
