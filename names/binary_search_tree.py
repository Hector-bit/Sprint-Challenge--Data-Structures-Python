# import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.storage = Queue()

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        # #if the self.value is empty
        # if self.value == None:
        #     #make the value a root node
        #     BinarySearchTree(value)
        # #if the tree is not empty
        # if self.value != None:
        #     #if the value is < to the root
        #     if value < self.value:
        #         #place value to the left
        #         if self.left == None:
        #             self.left = BinarySearchTree(value)
        #         else:
        #             self.left.insert(value)
        #         return
        #     #if the value is > to the root
        #     if value > self.value:
        #         #place value to the right
        #         if self.right == None:
        #             self.right = BinarySearchTree(value)
        #         else:
        #             # self.right == BinarySearchTree(value)
        #             self.right.insert(value)
        #         return


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        else:
            if target < self.value:
                if self.left == None:
                    return False
                else:
                    return self.left.contains(target)
            if target > self.value:
                if self.right == None:
                    return False
                else:
                    return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        #go right until you can't go right anymore and return that node
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value),
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node is None: 
            return
        queue = [] 
        queue.append(node) 
        while(len(queue) > 0): 
            print(queue[0].value), 
            node = queue.pop(0) 
            if node.left is not None: 
                queue.append(node.left) 
            if node.right is not None: 
                queue.append(node.right) 



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node: 
            print(node.value), 
            self.dft_print(node.left)  
            self.dft_print(node.right) 

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
