import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode


class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None        
        self.storage = None

    def enqueue(self, value):
        new_node = ListNode(value)
        self.size += 1
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.size != 0:            
            self.size -= 1
            node = self.head
            value = node.value
            self.head = node.next        
            node.delete()
            return value

    def len(self):
        return self.size
