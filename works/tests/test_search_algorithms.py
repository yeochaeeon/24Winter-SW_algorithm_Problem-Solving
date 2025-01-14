from src.search_algorithm import linear_search,binary_search
import unittest
class TestSearch(unittest.TestCase):
    def test_linear_search(self):
        self.assertEqual(linear_search([3,1,2],3),0)
        self.assertEqual(linear_search([1,2,3],6),-1)

    def test_binary_search(self):
        self.assertEqual(binary_search([1,2,3],3),2)
        self.assertEqual(binary_search([1,2,3],6),-1)

if __name__ == '__main__':
    unittest.main()