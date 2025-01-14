import unittest
from src.programmers import p42747, p87946, p12909, p42583, p43165


class TestProgrammers(unittest.TestCase):

    def test_p42747(self):
        self.assertEqual(p42747([3, 0, 6, 1, 5]), 3)

    def test_p87946(self):
        self.assertEqual(p87946(80, [[80, 20], [50, 40], [30, 10]]), 3)

    def test_p12909(self):
        self.assertEqual(p12909("()()"), True)
        self.assertEqual(p12909("(())()"), True)
        self.assertEqual(p12909(")()("), False)
        self.assertEqual(p12909("(()("), False)

    def test_p42583(self):
        self.assertEqual(p42583(2, 10, [7, 4, 5, 6]), 8)
        self.assertEqual(p42583(100, 100, [10]), 101)
        self.assertEqual(
            p42583(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110
        )

    def test_p43165(self):
        self.assertEqual(
            p43165([1, 1, 1, 1, 1], 3),
            5,
        )
        self.assertEqual(
            p43165([4, 1, 2, 1], 4),
            2,
        )


if __name__ == "__main__":
    unittest.main()
