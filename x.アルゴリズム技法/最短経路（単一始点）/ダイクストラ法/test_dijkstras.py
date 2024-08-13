import unittest
from dijkstras import run


class TestDijkstras(unittest.TestCase):

    def test_djkstras(self):
        """
        see: https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif
        """
        num_node = 6
        # [from, to, weight]
        edges = [
            [1, 2, 7],
            [1, 3, 9],
            [1, 6, 14],
            [2, 3, 10],
            [2, 4, 15],
            [3, 4, 11],
            [3, 6, 2],
            [4, 5, 6],
            [5, 6, 9]
        ]
        start = 1
        end = 5
        result = run(num_node, edges, start, end, True)
        self.assertEqual(20, result)

