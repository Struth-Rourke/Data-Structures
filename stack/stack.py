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

   The main difference between an array and a linked list that the elements in 
   the array can each be accessed individually, and at random, whereas elements 
   in a linked list must be accessed sequentially. Linked lists makes it more difficult
   to insert and remove items in the list because of the processing time it takes
   to move through all the elements sequentially just to get to the one item that
   is being asked to be returned. Not only that, but the elements in a linked list
   need to be adjusted based on where the element is being acccessed from since
   the order and pointers only go one way. 
"""


# 1. Array
class ListStack:

    def __init__ (self):
        # size
        self.size = 0
        # instantiate empty list
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        # add size
        self.size +=1
        # append value
        self.storage.append(value)
        # # add to front of array
        # self.storage.insert(0, value)
    
    def pop(self):
        if self.storage:
            return self.storage.pop()
            # # remove first element in storage
            # node = self.storage.pop(0)
            # return node.value
        # subtract size
        self.size -= 1
        else:
            return None

        # # alternate code
        # if len(self.storage) == 0:
            # return None
        # # remove first element in storage
        # self.size -= 1
        # node = self.storage.pop(0)
        # return node


# 2. Linked List
class Node:
    def __init__(self, value, next=None):
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
