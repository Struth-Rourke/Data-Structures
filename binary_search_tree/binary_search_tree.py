"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    # Insert the given value into the tree
    def insert(self, value):
        # if value < self.value (go left)
        if value < self.value:
            # if no left node
            if self.left is None:
                # insert left
                self.left = BSTNode(value)
            # left node found
            else: 
                # recursion to reiterate and check for another left node 
                self.left.insert(value)
        # if value > self.value (go right)
        else:
            # if no right node
            if self.right is None:
                # insert right
                self.right = BSTNode(value)
            # right node found
            else:
                # recursion to reiterare and check for another right node
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target equals value (return True)
        if target == self.value:
            # return True
            return True
        # if target less than value (go left)
        if target < self.value:
            # check isn't present
            if self.left is None:
                # False
                return False
            # check is present
            else:
                # recursion to check the left
                return self.left.contains(target)
        # elif target greater than value (go right)
        else:
            # check isn't present
            if self.right is None:
                # False
                return False
            # check is present
            else:
                # recursion to check the right
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        # check if right not present
        if self.right is None:
            # return value
            return self.value
        # check if is
        else:
            # recursion to test again since right is always highest
            return self.right.get_max()


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # applying the function to each found value
        fn(self.value)

        # depth-first search using recursion
        ## if left exists
        if self.left is not None:
            # recursively search for each left value
            self.left.for_each(fn)
        ## if right exists
        if self.right is not None:
            # recursively search for each right value
            self.right.for_each(fn)        


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # ### ALT CODE
        # # if node.left exists
        # if node.left is not None:
        #     # recursively call function to get to 'leftmost' node and value
        #     node.in_order_print(node.left)

        # # print 'leftmost' value
        # print(node.value)

        # # if node.right exists
        # if node.right is not None:
        #     # recursively call function to get to 'leftmost' node and value
        #     node.in_order_print(node.right)

        ### In-Order Recursive Traversals print in order of lowest to highest
        # if node doesn't exist
        if node is None:
            return 
        # if does exist
        else:
            # recursively check node.left (l)
            self.in_order_print(node.left)
            # print node.value (n)
            print(node.value)
            # recursively check node.right (r)
            node.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first (queue) traversal (FIFO) -- nested levels,
    # similar to a topograhical map with concentric rings
    def bft_print(self, node):
        # create queue
        queue = []
        # append node to queue
        queue.append(node)
        # while queue is True
        while queue:
            # first in, first out
            node = queue.pop(0)

            # print node value
            print(node.value)

            # enqueue next nodes
            ## if node.left exists
            if node.left is not None:
                # append to queue -- iterative breadth first traversal moves 
                # successively from left to right (across breadth) on the current 
                # tree level before moving to the next, lower level
                queue.append(node.left)
            ## if node.right exists
            if node.right is not None:
                # append to queue immediately AFTER left
                queue.append(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first (stack) traversal (LIFO)
    def dft_print(self, node):
        # set up stack
        stack = []
        # append node to current stack
        stack.append(node)
        # while stack is true
        while stack:
            # if node.left exists
            if node.left is not None:
                # append to stack
                stack.append(node.left)
            # if node.right exists
            if node.right is not None:
                # append to stack
                stack.append(node.right)

            # print node.value
            print(node.value)

            # node is popped off the stack
            node = stack.pop()


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # if node doesn't exist
        if node is None:
            return
        # if node does exist
        else:
            # print the value (n)
            print(node.value)
            # recursively check node.left (l)
            self.pre_order_dft(node.left)
            # recursively check node.right (r)
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is None:
            return
        else:
            # recursively check self.left (l)
            self.post_order_dft(node.left)
            # recursively check self.right (r)
            self.post_order_dft(node.right)
            # print node.value (n)
            print(node.value)
