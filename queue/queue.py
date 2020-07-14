"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?

    The main difference between an array and a linked list that the elements in 
    the array can each be accessed individually, and at random, whereas elements 
    in a linked list must be accessed sequentially. Linked lists makes it more difficult
    to insert and remove items in the list because of the processing time it takes
    to move through all the elements sequentially just to get to the one item that
    is being asked to be returned. Not only that, but the elements in a linked list
    need to be adjusted based on where the element is being acccessed from since
    the order and pointers only go one way. 
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


# 1. Array
class ListQueue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.storage:
            return self.storage.pop(0)


# 2. Linked List
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Class Queue
class Queue:
    def __init__(self):
        self.count = 0
        self.first = None
        self.last = None
    
    def __len__(self):
        return self.count

    def enqueue(self, value):
        # Instantiate 'node'
        node = Node(value)
        # If first element is 'None'
        if self.first is None:
            # Set it equal to first and last node in linked list
            self.first = node
            self.last = node
        else:
            # Set it equal to the next node
            self.last.next = node
            # Change the new next node to the last
            self.last = node
        # Add Count
        self.count += 1

    def dequeue(self):
        # If first is 'None'
        if self.first is None:
            return None
        # If first.next is 'None'
        elif self.first.next is None:
            # Set node as first
            node = self.first
            # Set '.first' as 'None'
            self.first = None
            # Set '.last' as 'None'
            self.last = None
            # Subtract Count
            self.count -= 1
            # Return 'node' value
            return node.value
        # Else
        else:
            # Set node as '.first'
            node = self.first
            # Set first as 'next'
            self.first = self.first.next
            # Subtract Count
            self.count -= 1
            # Return 'node' value
            return node.value
        