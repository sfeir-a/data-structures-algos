import unittest
from selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    
    def test_selection_sort_a(self):
        arr = [1]
        size = 1
        actual = selection_sort(arr, size)
        expected = [1]
        self.assertEqual(actual, expected)

    def test_selection_sort_b(self):
        arr = [9,6,2,4,5]
        size = 5
        actual = selection_sort(arr, size)
        expected = [2,4,5,6,9]
        self.assertEqual(actual, expected)

    def test_selection_sort_c(self):
        arr = list(range(1000,0,-1))
        size = 1000
        actual = selection_sort(arr, size)
        expected = list(range(1,1001))
        self.assertEqual(actual, expected)

    def test_selection_sort_empty(self):
        arr = []
        size = 0
        actual = selection_sort(arr, size)
        expected = []
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()