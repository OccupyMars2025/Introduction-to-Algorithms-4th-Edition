from typing import List


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def insert_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
    
    def build(self, lst: List[int]):
        for x in lst:
            self.insert_first(x)
            
    def __str__(self):
        string_repr = ""
        current_node = self.head
        while current_node is not None:
            string_repr += f"{current_node.data} --> "
            current_node = current_node.next
        string_repr += "None"
        return string_repr
    
    def to_list(self) -> List[int]:
        result = []
        current_node = self.head
        while current_node is not None:
            result.append(current_node.data)
            current_node = current_node.next
        return result


def reorder_students_v001(L: LinkedList) -> None:
    assert L.size % 2 == 0, "Linked list must have even number of elements"
    assert L.size >= 4
    
    n = L.size // 2
    current_node = L.head
    
    # """ 
    # maintain the loop invariant:
    # at the start of each iteration, current_node is the n-th node in the left half of the linked list.
    # Count from the n-th node to the 1-th node. (from right to left)
    
    # When the loop terminates, n is 1, current_node is the n-th node, i.e., the 1-th node.
    # """
    # use 1-index, find the n-th student
    while n > 1:
        current_node = current_node.next
        n -= 1
    
    # Just remember the location of the n-th node and (n+1)-th node
    # n-th node
    n_th_node = current_node
    # (n+1)-th node (the first element in the right half)
    n_plus_one_node = current_node.next
   
    prev_node = current_node
    current_node = current_node.next
    next_node = current_node.next
    
    # """ 
    # maintain the loop invariant:
    # before the start of each iteration, 
    # all the links after prev_node remain unchanged, 
    # all the links between the n-th node and prev_node are reversed.
    
    # so when the loop terminates, next_node is None, current_node is the last node, 
    # prev_node is the second last node.  According to the loop invariant, 
    # all the links between the n-th node and prev_node are reversed, 
    # all the links after prev_node remain unchanged. 
    # So after the loop terminates, we still need to reverse the last link 
    # between prev_node and current_node. 
    
    # What a crystal-clear explanation !!!
    # Just use the loop invariant to write correct code !!!
    # """
    while next_node is not None:
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
        next_node = next_node.next
        
    # Actually, you don't need this step, refer to reorder_students_v002()
    current_node.next = prev_node
        
    the_2n_th_node = current_node
    
    # final step
    n_th_node.next = the_2n_th_node
    n_plus_one_node.next = None
    
    
    

def reorder_students_v002(L: LinkedList) -> None:
    assert L.size % 2 == 0, "Linked list must have even number of elements"
    assert L.size >= 4
    
    n = L.size // 2
    current_node = L.head
    
    # """ 
    # maintain the loop invariant:
    # at the start of each iteration, current_node is the n-th node in the left half of the linked list.
    # Count from the n-th node to the 1-th node. (from right to left)
    
    # When the loop terminates, n is 1, current_node is the n-th node, i.e., the 1-th node.
    # """
    # use 1-index, find the n-th student
    while n > 1:
        current_node = current_node.next
        n -= 1
    
    # Just remember the location of the n-th node and (n+1)-th node
    # n-th node
    n_th_node = current_node
    # (n+1)-th node (the first element in the right half)
    n_plus_one_node = current_node.next
   
    prev_node = current_node
    current_node = current_node.next
    
    # """ 
    # maintain the loop invariant:
    # before the start of each iteration, 
    # all the links after prev_node remain unchanged, 
    # all the links between the n-th node and prev_node are reversed.
    
    # so when the loop terminates, current_node is None, prev_node is the last node.
    #   According to the loop invariant, 
    # all the links between the n-th node and prev_node are reversed, 
    # all the links after prev_node remain unchanged. 
    # So after the loop terminates, we don't need to reverse the last link    
    #
    # What a crystal-clear explanation !!!
    # Just use the loop invariant to write correct code !!!
    # """
    while current_node is not None:
        current_node.next = prev_node
        # prev_node, current_node = current_node, current_node.next
        prev_node = current_node
        current_node = current_node.next
            
    the_2n_th_node = prev_node
    
    # final step
    n_th_node.next = the_2n_th_node
    n_plus_one_node.next = None



def reorder_students_v003(L: LinkedList) -> None:
    """ 
    reorder_students_v002() is buggy, it doesn't 
    fetch the next_node before "current_node.next = prev_node" in the while loop.
    
    This version is fixed.
    """
    assert L.size % 2 == 0, "Linked list must have even number of elements"
    assert L.size >= 4
    
    n = L.size // 2
    current_node = L.head
    
    # """ 
    # maintain the loop invariant:
    # at the start of each iteration, current_node is the n-th node in the left half of the linked list.
    # Count from the n-th node to the 1-th node. (from right to left)
    
    # When the loop terminates, n is 1, current_node is the n-th node, i.e., the 1-th node.
    # """
    # use 1-index, find the n-th student
    while n > 1:
        current_node = current_node.next
        n -= 1
    
    # Just remember the location of the n-th node and (n+1)-th node
    # n-th node
    n_th_node = current_node
    # (n+1)-th node (the first element in the right half)
    n_plus_one_node = current_node.next
   
    prev_node = current_node
    current_node = current_node.next
    
    # """ 
    # maintain the loop invariant:
    # before the start of each iteration, 
    # all the links after prev_node remain unchanged, 
    # all the links between the n-th node and prev_node are reversed.
    
    # so when the loop terminates, current_node is None, prev_node is the last node.
    #   According to the loop invariant, 
    # all the links between the n-th node and prev_node are reversed, 
    # all the links after prev_node remain unchanged. 
    # So after the loop terminates, we don't need to reverse the last link    
    #
    # What a crystal-clear explanation !!!
    # Just use the loop invariant to write correct code !!!
    # """
    while current_node is not None:
        # fetch the next_node before "current_node.next = prev_node"
        next_node = current_node.next
        current_node.next = prev_node
        prev_node, current_node = current_node, next_node
        
            
    the_2n_th_node = prev_node
    
    # final step
    n_th_node.next = the_2n_th_node
    n_plus_one_node.next = None

   

def test_reorder_students():
    import random
    for n in range(2, 1000):
        lst_001 = random.choices(range(1000), k=2*n)
        lst_002 = list(lst_001)
        llist_001 = LinkedList()
        llist_001.build(lst_001)
        llist_002 = LinkedList()
        llist_002.build(lst_002)
        # print("before:", llist)
        reorder_students_v001(llist_001)
        # reorder_students_v002(llist)
        reorder_students_v003(llist_002)
        # print("after :", llist)
        assert llist_001.to_list() == llist_002.to_list()

if __name__ == '__main__':
    test_reorder_students()