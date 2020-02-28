from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.size = 0

    def append(self, item):
        #if capacity is 0 then add a new node
        # if self.size == 0:
        #     self.storage.add_to_head(item)
        #     self.size += 1
        #if capacity is not 0 or 10 then add it to the head
        if self.size < self.capacity:
            self.storage.add_to_head(item)
            self.size += 1
        #if capacity is 10 then add to front and remove last node
        elif self.size == self.capacity:
            self.storage.remove_from_tail()
            self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # if self.current != None:
        #     list_buffer_contents
        for i in range(self.size + 1):
            if self.current != None:
                list_buffer_contents.append(self.current.value)
            if i < self.capacity:
                if self.current:
                    self.current = self.current.prev
                elif self.current == None:
                    self.current = self.storage.tail

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
