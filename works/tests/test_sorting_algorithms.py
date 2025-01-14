from src.sorting_algorithm import bubble_sort,quick_sort, merge_sort
import unittest

class TestSorting(unittest.TestCase):
    def test_bubble(self):
        self.assertEqual(bubble_sort([]),[]) # edge case
        self.assertEqual(bubble_sort([1]),[1]) # edge case
        self.assertEqual(bubble_sort([3,2,1]), [1,2,3])
        self.assertEqual(bubble_sort([3,2,1,4]),[1,2,3,4])
        self.assertEqual(bubble_sort([-3,2,-1,4]),[-3,-1,2,4]) # 음수 케이스 
        self.assertEqual(bubble_sort([3,2,1,4,5,9,8,7,6]),[1,2,3,4,5,6,7,8,9])
    def test_quick_sort(self):
        self.assertEqual(quick_sort([]),[]) # edge case
        self.assertEqual(quick_sort([1]),[1]) # edge case
        self.assertEqual(quick_sort([3,2,1]), [1,2,3])
        self.assertEqual(quick_sort([3,2,1,4]),[1,2,3,4])
        self.assertEqual(quick_sort([-3,2,-1,4]),[-3,-1,2,4]) # 음수 케이스 
        self.assertEqual(quick_sort([3,2,1,4,5,9,8,7,6]),[1,2,3,4,5,6,7,8,9])
        self.assertEqual(quick_sort([5,4,3,2,1]),[1,2,3,4,5])
    def test_merge_sort(self):
        self.assertEqual(merge_sort([]),[]) # edge case
        self.assertEqual(merge_sort([1]),[1]) # edge case
        self.assertEqual(merge_sort([3,2,1]), [1,2,3])
        self.assertEqual(merge_sort([3,2,1,4]),[1,2,3,4])
        self.assertEqual(merge_sort([-3,2,-1,4]),[-3,-1,2,4]) # 음수 케이스 
        self.assertEqual(merge_sort([3,2,1,4,5,9,8,7,6]),[1,2,3,4,5,6,7,8,9])
        self.assertEqual(merge_sort([5,4,3,2,1]),[1,2,3,4,5])

if __name__ == '__main__':
    unittest.main()