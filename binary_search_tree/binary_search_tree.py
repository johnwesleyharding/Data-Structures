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
            
    def contains(self, target):
        
        if self.value < target and self.right:
            
            return self.right.contains(target)
        
        if self.value > target and self.left:
            
            return self.left.contains(target)
        
        if self.value == target:
            
            return True
        
        return False

    def get_max(self):
        
        if self.right:
            
            return self.right.get_max()
            
        return self.value

    def for_each(self, cb):
        
        if self.left:
            
            self.left.for_each(cb)
            
        if self.right:
            
            self.right.for_each(cb)
            
        cb(self.value)

    def in_order_print(self, node):
        
        if self.left:
            
            self.left.in_order_print(self.left)
        
        print(self.value)
        
        if self.right:
            
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        
        nodes = [[node, 0]]
        depth = 0
        prints = []
        
        while len(nodes) > 0:
            
            if nodes[depth][1] == 0:
                
                if len(prints) < depth + 1:
                    
                    prints.append([nodes[depth][0].value])
                    
                else:
                    
                    prints[depth].append(nodes[depth][0].value)
                
                nodes[depth][1] += 1
                
                if nodes[depth][0].left:
                    
                    nodes.append([nodes[depth][0].left, 0])
                    depth += 1
                
            elif nodes[depth][1] == 1:
                
                nodes[depth][1] += 1
                
                if nodes[depth][0].right:
                    
                    nodes.append([nodes[depth][0].right, 0])
                    depth += 1
            
            else:
                
                nodes.pop(-1)
                depth -= 1
                
        for depth in prints:
                
            for value in depth:
                    
                print(value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        
        nodes = [[node, 0]]
        depth = 0
        
        while len(nodes) > 0:
            
            if nodes[depth][1] == 0:
                
                print(nodes[depth][0].value)
                nodes[depth][1] += 1
                
                if nodes[depth][0].left:
                    
                    nodes.append([nodes[depth][0].left, 0])
                    depth += 1
                
            elif nodes[depth][1] == 1:
                
                nodes[depth][1] += 1
                
                if nodes[depth][0].right:
                    
                    nodes.append([nodes[depth][0].right, 0])
                    depth += 1
            
            else:
                
                nodes.pop(-1)
                depth -= 1

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass