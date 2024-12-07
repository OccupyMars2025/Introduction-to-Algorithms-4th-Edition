from typing import List

class MinHeap:
    def __init__(self, array: List[int]):
        self.array = array
        self.heap_size = len(array)
    
    def left(self, i: int) -> int:
        return 2 * i + 1
    
    def right(self, i: int) -> int:
        return 2 * i + 2
    
    def parent(self, i: int) -> int:
        return (i - 1) // 2
    
    def min_heapify(self, i: int) -> None:
        """
        We assume that the subtrees rooted at nodes left(i) 
        and right(i) are both min heaps before we call min_heapify(i).

        Args:
            i (int): node index in the array
        """
        l = self.left(i)
        r = self.right(i)
        smallest = i
        
        # Check if left child exists and is less than root
        if l < self.heap_size and self.array[l] < self.array[smallest]:
            smallest = l
        
        # Check if right child exists and is less than smallest so far
        if r < self.heap_size and self.array[r] < self.array[smallest]:
            smallest = r
        
        # If largest is not root
        if smallest != i:
            self.array[i], self.array[smallest] = self.array[smallest], self.array[i]  # Swap
            self.min_heapify(smallest)

# Example usage
if __name__ == "__main__":
    arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    heap = MinHeap(arr)
    heap.min_heapify(0)
    print(heap.array)