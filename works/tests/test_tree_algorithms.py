import unittest
from src.tree_algorithm import (
    preorder,
    inorder,
    postorder,
    preorder_iter,
    inorder_iter,
    postorder_iter,
    preorder_stack,
    inorder_stack,
    postorder_stack,
)


class TestTreehAlgorithms(unittest.TestCase):

    def test_binary_tree_iter_traversal(self):
        input_tree = ["A", "B", "C", "D", "E", "F", None, "G"]
        self.assertEqual(
            preorder_iter(input_tree, 0), ["A", "B", "D", "G", "E", "C", "F"]
        )
        self.assertEqual(
            inorder_iter(input_tree, 0), ["G", "D", "B", "E", "A", "F", "C"]
        )
        self.assertEqual(
            postorder_iter(input_tree, 0), ["G", "D", "E", "B", "F", "C", "A"]
        )

    def test_binary_tree_stack_traversal(self):
        input_tree = ["A", "B", "C", "D", "E", "F", None, "G"]
        self.assertEqual(
            preorder_stack(input_tree), ["A", "B", "D", "G", "E", "C", "F"]
        )
        self.assertEqual(inorder_stack(input_tree), ["G", "D", "B", "E", "A", "F", "C"])
        self.assertEqual(
            postorder_stack(input_tree), ["G", "D", "E", "B", "F", "C", "A"]
        )

    def test_binary_tree_traversal(self):
        input_tree = ["A", "B", "C", "D", "E", "F", None, "G"]
        self.assertEqual(preorder(input_tree, 0), ["A", "B", "D", "G", "E", "C", "F"])
        self.assertEqual(inorder(input_tree, 0), ["G", "D", "B", "E", "A", "F", "C"])
        self.assertEqual(postorder(input_tree, 0), ["G", "D", "E", "B", "F", "C", "A"])


if __name__ == "__main__":
    unittest.main()
