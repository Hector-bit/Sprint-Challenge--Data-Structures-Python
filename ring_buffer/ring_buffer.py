from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.size = 0

    def append(self, item):
        if self.size == 0:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
            self.size += 1
            # print(self.storage.__len__(), 'ERWGQNIOVWEG')
            # print(self.storage.head.value, 'LJZHXF')
        elif self.size < self.capacity:
            self.storage.add_to_tail(item)
            self.storage.tail.next = self.storage.head
            self.size += 1
        else:
            self.current.value = item
            self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
        current = self.storage.head
        while current is not self.storage.tail:
            list_buffer_contents.append(current.value)
            current = current.next
        list_buffer_contents.append(self.storage.tail.value)

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
