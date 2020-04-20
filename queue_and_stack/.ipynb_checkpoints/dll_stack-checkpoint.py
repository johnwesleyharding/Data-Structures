import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def push(self, value):
        self.size += 1
        self.storage.insert(0, value)

    def pop(self):
        if self.size != 0:
            self.size -= 1
            return self.storage.pop(0)

    def len(self):
        return self.size
