from typing import List

class MaxHeap:
    def __init__(self, array: List[int]):
        self.array = array
        self.heap_size = len(array)
    
    def left(self, i: int) -> int:
        return 2 * i + 1
    
    def right(self, i: int) -> int:
        return 2 * i + 2
    
    def parent(self, i: int) -> int:
        return (i - 1) // 2
    
    def heapsort(self) -> None:
        self.build_max_heap()
        for i in range(self.heap_size-1, 0, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.heap_size -= 1
            self.max_heapify(0)
    
    def build_max_heap(self) -> None:
        assert self.heap_size == len(self.array)
        for i in range(self.parent(self.heap_size-1), -1, -1):
            self.max_heapify(i)
    
    def max_heapify(self, i: int) -> None:
        """
        We assume that the subtrees rooted at nodes left(i) 
        and right(i) are both max heaps before we call max_heapify(i).

        Args:
            i (int): node index in the array
        """
        l = self.left(i)
        r = self.right(i)
        largest = i
        
        # Check if left child exists and is greater than root
        if l < self.heap_size and self.array[l] > self.array[largest]:
            largest = l
        
        # Check if right child exists and is greater than largest so far
        if r < self.heap_size and self.array[r] > self.array[largest]:
            largest = r
        
        # If largest is not root
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]  # Swap
            self.max_heapify(largest)
            
    def max_heapify_iterative_version(self, i: int) -> None:
        """
        We assume that the subtrees rooted at nodes left(i) 
        and right(i) are both max heaps before we call this method.

        Args:
            i (int): node index in the array
        """
        while True:
            l = self.left(i)
            r = self.right(i)
            largest = i
            
            # Check if left child exists and is greater than root
            if l < self.heap_size and self.array[l] > self.array[largest]:
                largest = l
            
            # Check if right child exists and is greater than largest so far
            if r < self.heap_size and self.array[r] > self.array[largest]:
                largest = r
            
            # If largest is not root
            if largest != i:
                self.array[i], self.array[largest] = self.array[largest], self.array[i]  # Swap
                i = largest
            else:
                break

# Example usage
if __name__ == "__main__":
    arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    heap = MaxHeap(arr)
    heap.max_heapify(0)
    print(heap.array)