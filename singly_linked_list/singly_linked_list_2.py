# Creating Class
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_values(self):
        return self.value

    def get_next(self):
        return self.get_next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.count = 0
        # first node in the list
        self.head = None
        # last node in the list
        self.tail = None

    def add_to_head(self, value):
        '''
        Add a new Node to the tail of the list.
        '''
        # instantiate 'new_node'
        new_node = Node(value)

        # if the list is empty
        if self.head is None and self.tail is None:
            # save to head
            self.head = new_node
            # save to tail
            self.tail = new_node
            self.count += 1
        else:
            # new_node should point to current head
            new_node.next = self.head
            # move head to new_node
            self.head = new_node
            # add count
            self.count += 1

    
    def add_to_tail(self, value):
        '''
        Add a new Node to the tail of the list.
        '''
        # Instantiate 'new_node'
        new_node = Node(value)

        # If the list is empty
        if self.head is None and self.tail is None:
            # save to head
            self.head = new_node
            # save to tail
            self.tail = new_node
            # add count
            self.count += 1
        else:
            # point node at the current tail to new_node
            self.tail.next = new_node
            # move tail to new_node
            self.tail = new_node
            # add count
            self.count += 1
