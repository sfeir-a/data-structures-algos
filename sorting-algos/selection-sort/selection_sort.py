import random
import time

def selection_sort(arr, size):
    for i in range(size):
        temp = i
        for j in range(i+1,size):
            if arr[j] < arr[temp]:
                temp = j
        arr[i], arr[temp] = arr[temp], arr[i]
    return arr

if __name__ == "__main__":
    arr = []
    size = 1000
    for i in range(size):
        arr.append(random.randint(1,10000))

    # timing from: https://stackoverflow.com/questions/14452145/how-to-measure-time-taken-between-lines-of-code-in-python 
    start = time.time()
    arr_sorted = selection_sort(arr, size)
    end = time.time()
    time_took = end - start
    print("Code took " + str(time_took))

    print("Array is equal: " + str(arr_sorted == sorted(arr)))
