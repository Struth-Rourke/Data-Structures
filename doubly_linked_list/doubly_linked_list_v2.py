"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def insert_after(self, value):
        # tracker for next
        current_next = self.next
        # setting next as ListNode
        self.next = ListNode(value, self, current_next)
        # if exists
        if current_next:
            # set prev as next
            current_next.prev = self.next

    def insert_before(self, value):
        # current_prev as prev
        current_prev = self.prev
        # prev equal to ListNode
        self.prev = ListNode(value, current_prev, self)
        # if true
        if current_prev:
            # next equals prev
            current_prev.next = self.prev
            
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # if list is empty
        if self.head is None:
            node = ListNode(value)
            self.head = node
            self.tail = node
        else:
            # node 'insert_before' and update pointers
            self.head.insert_before(value)
            # head equal to prev
            self.head = self.head.prev
        # add length
        self.length += 1
            
            
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        return self.delete(self.head)
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # if list is empty
        if self.tail is None:
            # creating node
            node = ListNode(value)
            # save to head
            self.head = node
            # save to tail
            self.tail = node
        else:
            # use node insert after and update pointers
            self.tail.insert_after(value)
            # setting tail as next
            self.tail = self.tail.next
        # add length
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        return self.delete(self.tail)
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # deleting the node
        self.delete(node)
        # moving node value to the head
        self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # deleting the node
        self.delete(node)
        # moving node value to the tail
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # if list is empty
        if self.head is None:
            return None
        # if only one node
        elif node == self.head and node == self.tail:
            # set head none
            self.head = None
            # set tail none
            self.tail = None
        # if node is head
        elif node == self.head:
            # delete head
            self.head.delete()
            # set head as next
            self.head = self.head.next
        # if node is tail
        elif node == self.tail:
            # delete tail
            self.tail.delete()
            # set tail as prev
            self.tail = self.tail.prev
        # node in middle of list
        else:
            node.delete()
        # because only the no nodes if returns, I can put this here
        # to cover decrementing the length for all other cases
        self.length -= 1
        return node.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # set tracker as head
        current = self.head
        # create max_value
        max_value = 0
        # current is None
        if current is None:
            return None
        # while loop
        while True:
            # Update value if larger
            if max_value < current.value:
                # set max_value as value
                max_value = current.value

            # break infinite loop
            if current.next is None:
                break
            # current tracker set as next
            current = current.next
        # return max_value
        return max_value