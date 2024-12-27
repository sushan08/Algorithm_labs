import unittest
from sort import merge_sort, quick_sort

class TestSort(unittest.TestCase):
    def test_merge_sort(self):
        A = [3, 41, 52, 26, 38, 57, 9, 49]
        sorted_A = [3, 9, 26, 38, 41, 49, 52, 57]
        merge_sort(A, 0, len(A) - 1)
        self.assertListEqual(A, sorted_A)

    def test_quick_sort(self):
        A = [3, 41, 52, 26, 38, 57, 9, 49]
        sorted_A= [3, 9, 26, 38, 41, 49, 52, 57]
        quick_sort(A, 0, len(A) - 1)
        self.assertListEqual(A,sorted_A)

if __name__ == "__main__":
    unittest.main()