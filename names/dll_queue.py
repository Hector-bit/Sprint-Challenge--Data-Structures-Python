# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Because  of the large amount of insertions and deletions
        # You shouldn't use an array for the queue because each insertion could re-allocate new space
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        return self.storage.add_to_head(value)

    def dequeue(self):
        return self.storage.remove_from_tail()

    def len(self):
        return self.storage.length