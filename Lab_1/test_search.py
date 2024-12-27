import unittest
from search import linear_search, binary_search

class SearchTestCase(unittest.TestCase):
    def test_linear_search(self): 
        values = [7, 5, 6, 8, 3, 2, 1] 
        result = linear_search(values, 1) 
        self.assertEqual(result, 6)
        self.assertEqual(linear_search(values, 7), 0)
        self.assertEqual(linear_search(values, 8), 3)

def test_binary_search(self):
    values = [7, 5, 6, 8, 3, 2, 1]
    values.sort()
    result = binary_search(values, 1) 
    self.assertEqual(result, 6)
    self.assertEqual(binary_search(values, 7), 0)
    self.assertEqual(binary_search(values, 8), 3)

if __name__ == '__main__':
    unittest.main()
