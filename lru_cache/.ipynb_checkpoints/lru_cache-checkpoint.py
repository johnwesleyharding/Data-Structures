import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode

class LRUCache:

    def __init__(self, limit=10):
        
        self.limit = limit
        self.ordering = DoublyLinkedList()
        self.storage = {}
        self.size = 0

    def get(self, key):
        
        if key in self.storage:
            
            node = self.storage[key]
            self.ordering.move_to_front(node)            
            return node.value[1]

        else:
            
            return None

    def set(self, key, value):
        
        if key in self.storage:
            
            node = self.storage[key]
            node.value = (key, value)
            self.ordering.move_to_front(node)
            return
        
        if self.size == self.limit:
            
            oldest_key = self.ordering.tail.value[0]
            del self.storage[oldest_key]
            self.ordering.remove_from_tail()
            self.size -=1
        
        self.ordering.add_to_head((key, value))
        self.storage[key] = self.ordering.head
        self.size += 1