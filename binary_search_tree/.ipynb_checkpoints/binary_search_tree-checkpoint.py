import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    
    def __init__(self, value):
        
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        
        if value < self.value:
            
            if self.left:
                
                self.left.insert(value)
                
            else:
                
                self.left = BinarySearchTree(value)
            
        else:
            
            if self.right:
                
                self.right.insert(value)
                
            else:
                
                self.right = BinarySearchTree(value)
            
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        if self.value < target and self.right:
            
            return self.right.contains(target)
        
        if self.value > target and self.left:
            
            return self.left.contains(target)
        
        if self.value == target:
            
            return True
        
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        
        if self.right:
            
            return self.get_max()
            
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        
        if self.left:
            
            self.left.for_each(cb)
            
        if self.right:
            
            self.right.for_each(cb)
            
        cb(self)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        
        if self.left:
            
            self.in_order_print(self.left)
        
        print(self.value)
        
        if self.right:
            
            self.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        
        print(self.value)
        
        depth = self.left or self.right
        opts = ['left', 'right']
        
        while depth > 0:
            
            print(getattr('self' + '.left' * depth + '.value'))
                
                
            
            
            
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass