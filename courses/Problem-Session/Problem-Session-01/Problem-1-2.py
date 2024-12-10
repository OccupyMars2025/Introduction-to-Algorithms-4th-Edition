class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class D:
    def __init__(self):
        pass
    
    def insert_first(self, x):
        raise NotImplementedError
        
    def insert_last(self, y):
        raise NotImplementedError
        
    def delete_first(self) -> Node:
        raise NotImplementedError
        
    def delete_last(self) -> Node:
        raise NotImplementedError
    
    def __len__(self):
        raise NotImplementedError
    
    def swap_ends(self):
        assert len(self) >= 2
        first_node = self.delete_first()
        last_node = self.delete_last()   
        self.insert_first(last_node)
        self.insert_last(first_node)
        
    def shift_left(self, k: int):
        assert 1 <= k < len(self)
        while k > 0:
            first_node = self.delete_first()
            self.insert_last(first_node)
            k -= 1