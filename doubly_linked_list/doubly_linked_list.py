"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

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
        # creating new_node
        new_node = ListNode(value, None, None)
        # add length
        self.length += 1
        # if list is empty
        if not self.head and not self.tail:
            # save head as new_node
            self.head = new_node
            # save tail as new_node
            self.tail = new_node
        else:
            # set new_node.next as head
            new_node.next = self.head
            # head and prev as new_node
            self.head.prev = new_node
            # head as new_node
            self.head = new_node

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # creating value variable
        value = self.head.value
        # deleting head
        self.delete(self.head)
        # returning value
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # creating new_node
        new_node = ListNode(value, None, None)
        # add length
        self.length += 1
        # if not tail and head
        if not self.tail and not self.head:
            # tail as new_node
            self.tail = new_node
            # head as new_node
            self.head = new_node
        else:
            # prev node as tail
            new_node.prev = self.tail
            # tail next as new_node
            self.tail.next = new_node
            # tail as new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # tracker of tail value
        value = self.tail.value
        # deleting the tail
        self.delete(self.tail)
        # returning tracker
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # if is head
        if node is self.head:
            return
        # value tracker
        value = node.value
        # if is tail
        if node is self.tail:
            # remove_from_tail
            self.remove_from_tail()
        else:
            # delete node
            node.delete()
            # subtract length
            self.length -= 1
        # add_to_head
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # if is tail
        if node is self.tail:
            return
        # value tracker
        value = node.value
        # if is head
        if node is self.head:
            # remove from head
            self.remove_from_head()
            # add to tail
            self.add_to_tail(value)
        else:
            # delete node
            node.delete()
            # subtract length
            self.length -= 1
            # add_to_tail
            self.add_to_tail(value)


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # subtract length
        self.length -= 1
        # if list is empty
        if not self.head and not self.tail:
            return None
        # if head == tail
        if self.head == self.tail:
            # set as None
            self.head = None
            self.tail = None
        # if head == node
        elif self.head == node:
            # head = next
            self.head = node.next
            # delete node
            node.delete()
        # if tail == node
        elif self.tail == node:
            # change tail to prev
            self.tail = node.prev
            # delete node
            node.delete()
        else:
            # delete
            node.delete()


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # if list is empty
        if not self.head:
            return None
        # max_value is equal to head value
        max_value = self.head.value
        # tracker variable starting at head
        current = self.head
        # while loop
        while current:
            # if current value is greater than max_value
            if current.value > max_value:
                # updated max_value with current value
                max_value = current.value
            # otherwise move to next
            current = current.next
        # return max_value
        return max_value
