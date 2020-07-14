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

    def contains(self, value):
        # check if list is present
        if self.head is None:
            return False
        else:
            # start pointer at head
            current_node = self.head
            # iterate through the list
            while True:
                # check if values are equal 
                if current_node.value == value:
                    # if True, return it
                    return True
                # break loop if next is None
                if current_node.next is None:
                    break
                
                # move pointer and current_node
                current_node = current_node.next
            # not in the list, return False
            return False
        

    def remove_head(self):
        # return number like '.pop()'
        # check head is None
        if self.head is None:
            # return None
            return None
        # check head.next is not None 
        elif self.head.next is not None:
            # set variable for value
            val = self.head.value
            # set head as next
            self.head = self.head.next
            # subtract count
            self.count -= 1
            # return val
            return val
        # if only head present
        else:
            # set variable for value
            val = self.head.value
            # set head None
            self.head = None
            # set tail None
            self.tail = None
            # subtract count
            self.count -= 1
            # return val
            return val
    
    def get_max(self):
        # list exist? if None
        if self.head is None:
            return None
        # if it does exist
        else:
            # set pointer (current_node) to head 
            current_node = self.head
            # create max_value variable
            max_value = 0
            while True:
                # check inequality
                if max_value < current_node.value:
                    # set value as maxval if larger
                    max_value = current_node.value
                # break if there is no next
                if current_node.next is None:
                    break
                # move pointer and current_node
                current_node = current_node.next
            # return max_value
            return max_value
