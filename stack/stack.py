"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

   
"""


# 1. Array
class ListStack:

    def __init__ (self):
        # Size
        self.size = 0
        # Instantiate empty list
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        # append value
        self.storage.append(value)
    
    def pop(self):
        if self.storage:
            return self.storage.pop()
        else:
            return None


# 2. Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = next


# Linked List -- Stack
class Stack:
    def __init__(self):
        # count
        self.count = 0
        # '.first'
        self.first = None

    def __len__(self):
        return self.count

    def push(self, value):
        # if '.first' is None?
        if self.first is None:
            # '.first' = Node
            self.first = Node(value)
        # else?
        else:
            # the first node becomes the next node 
            node = Node(value, next=self.first)
            # replacing the first with the new node
            self.first = node
        # add count
        self.count += 1

    def pop(self):
        # if '.first' is None?
        if self.first is None:
            return None
        # elif '.first.next' is None?
        elif self.first.next is None:
            # node becomes '.first'
            node = self.first
            # replace with none because we are popping 
            self.first = None
            # subtract Count
            self.count -= 1
            # return 'pop' value
            return node.value
        # else?
        else:
            # node is .first'
            node = self.first
            # .'first' becomes '.first.next'
            self.first = self.first.next
            # subtract count
            self.count -= 1
            # return
            return node.value
