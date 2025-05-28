import sys

class MaxHeap:
    def __init__(self, max_size): 
            self.max_size = max_size
            self.size = 0
            self.Heap = [0] * (self.max_size + 1)
            #self.Heap[0] = float("inf")
            self.Heap[0] = sys.maxsize
            self.FRONT = 1

    @staticmethod
    def parent(k):   
        return k / 2
    
    @staticmethod
    def left(k):  
        return 2 * k

    @staticmethod
    def right(k):  
        return (2 * k) + 1  

    def swap(self, x, y):
        self.Heap[x], self.Heap[y] = (self.Heap[y], self.Heap[x])

    
    def max_heap_insert(self, x):
        self.size += 1
        i = self.size
        self.Heap[i] = x

        while (i > 1) and (self.Heap[self.parent(i)] < self.Heap[i]):
            self.swap(self, self.Heap[i], self.Heap[self.parent(i)])
            i = self.parent(i)

    def max_heapify(self, size):
        done = False
        j = 1

        while not done:
            L = self.left(j)
            R = self.right(j)
            largest = j

            if (L <= size) and (self.Heap[L] > self.Heap[largest]):
                largest = L
            if (R <= size) and (self.Heap[R] > self.Heap[largest]):
                largest = R
            if j != largest:
                self.swap(self.Heap[j], self.Heap[largest])
            else:
                done = True
            j = largest

    def heap_extract_max(self, size):
        if size < 1:
            print("error: heap underflow")
        
        maxKey = self.Heap[1]
        self.Heap[1] = self.Heap[size]
        size = size - 1
        self.max_heapify(self, size)
        return maxKey



if __name__ == "__main__":
    maxHeap = MaxHeap(15)
    maxHeap.max_heap_insert(5)
    maxHeap.max_heap_insert(7)
    maxHeap.max_heap_insert(3)