import unittest
from src.stack_queue_algorithm import (
    is_valid_parentheses,
    infix_to_prefix,
)


class TestStackQuickAlgorithms(unittest.TestCase):

    def test_valid_parentheses(self):
        self.assertEqual(is_valid_parentheses("{[()]}"), True)
        self.assertEqual(is_valid_parentheses("{[())}"), False)

    def test_infix_to_prefix(self):
        expression = "A + B * C / ( D + E )"
        self.assertEqual(infix_to_prefix(expression), "+ A / * B C + D E")


if __name__ == "__main__":
    unittest.main()
