import unittest
from src.bfs_dfs_algorithm import bfs, dfs


class TestBFSDFSAlgorithms(unittest.TestCase):

    def setUp(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["D", "E"],
            "C": ["F", "G"],
            "D": [],
            "E": [],
            "F": [],
            "G": [],
        }
        return super().setUp()

    def test_bfs(self):
        self.assertEqual(bfs(self.graph, "A"), ["A", "B", "C", "D", "E", "F", "G"])

    def test_dfs(self):
        self.assertEqual(dfs(self.graph, "A"), ["A", "C", "G", "F", "B", "E", "D"])
