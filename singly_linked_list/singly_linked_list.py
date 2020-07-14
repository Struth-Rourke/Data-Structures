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
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        '''
        Add a new Node to the tail of the list.
        '''
        # Instantiate 'new_node'
        new_node = Node(value)

        # If the list is empty, save to both the head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.count += 1
        else:
            # append it to the tail
            self.tail.next = new_node
            self.tail = new_node
            self.count += 1

        

# ll = Node(1)
# ll.set_next(Node(2))
# ll.next.set_next(Node(3))
# ll.next.next.set_next(Node(4))
# ll.next.next.next.set_next(Node(5))
    

