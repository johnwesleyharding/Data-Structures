class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
four = Node(4)
three = Node(3, four)
two = Node(2, three)
one = Node(1, two)
head_node = Node(0, one)

def find_middle(head):
    
    fast_pointer = head
    slow_pointer = head
    
    while fast_pointer.next is not None:
        
        fast_pointer = fast_pointer.next
        
        if fast_pointer.next is None:
            
            return slow_pointer
        
        fast_pointer = fast_pointer.next
        slow_pointer = slow_pointer.next
        
    return slow_pointer

print(find_middle(head_node).value)

# def reverse(head):
#     a = head
#     b = a.next
#     a.next = None
#     while True:
#         if b.next == None:
#             b.next = a
#             return b
#         c = b.next
#         b.next = a
#         a = b
#         b = c

def reverse(head):
    a = head
    b = a.next
    a.next = None
    while True:
        if b.next == None:
            b.next = a
            return b
        b.next = a
        b = a

reverse(head_node)
for node in [head_node, one, two, three, four]:
    print(node.value, node.next.value)