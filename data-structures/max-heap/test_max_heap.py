import unittest
from max_heap import MaxHeap


class TestSelectionSort(unittest.TestCase):
    
    def test_max_heap_insert(self):
        maxHeap = MaxHeap(1)
        maxHeap.max_heap_insert(5)
        actual = maxHeap.Heap
        expected = [0,5]
        self.assertEqual(actual, expected)


    

if __name__ == '__main__':
    unittest.main()