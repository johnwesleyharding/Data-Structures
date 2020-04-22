import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode

class LRUCache:

    def __init__(self, limit=10):
        
        self.limit = limit
        self.ordering = DoublyLinkedList()
        self.storage = {}
        self.size = 0
        
#         self.limit = limit
#         self.length = 0
#         self.recent = DoublyLinkedList()
#         self.data = {}

    def get(self, key):
        
        if key in self.storage:
            
            node = self.storage[key]
            self.ordering.move_to_front(node)            
            return node.value # node.value[1]

        else:
            
            return None
        
#         self.recent.move_to_front(key)
#         return self.data[key]

    def set(self, key, value):
        
        if key in self.storage:
            
            node = self.storage[key]
            node.value = value # (key, value)
            self.ordering.move_to_front(node)
            return
        
        if self.size == self.limit:
            
            oldest_key = self.ordering.tail.value
            del self.storage[oldest_key]
            self.ordering.remove_from_tail()
            self.size -=1
        
        self.ordering.add_to_head(value)
        self.storage[key] = self.ordering.head
        self.size += 1
        
#         self.recent.add_to_head(key)        
#         self.data[key] = value
