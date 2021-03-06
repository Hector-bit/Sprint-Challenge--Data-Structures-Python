"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        current = self.head
        s = ''
        while current is not None:
            s += str(current.value) + " "
            current = current.next
        return s

    def add_to_head(self, value):
        """Wraps the given value in a ListNode and inserts it
        as the new head of the list. Don't forget to handle
        the old head node's previous pointer accordingly."""
        self.length += 1
        # if this is an empty list
        if not self.head and not self.tail:
            self.head = self.tail = ListNode(value)
        else:
            # otherwise proceed normally
            # insert_before also takes care of the changing pointers
            self.head.insert_before(value)
            # set the list head to the newly created node (already inserted before the head)
            self.head = self.head.prev

    def remove_from_head(self):
        """Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node."""
        # delete current head node
        if not self.head:
            return None
        value = self.head.value
        self.delete(self.head)
        return value

    def add_to_tail(self, value):
        """Wraps the given value in a ListNode and inserts it
        as the new tail of the list. Don't forget to handle
        the old tail node's next pointer accordingly."""
        # similar to add_to_head
        self.length += 1
        if not self.head and not self.tail:
            self.tail = self.head = ListNode(value)
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

    def remove_from_tail(self):
        """Removes the List's current tail node, making the
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node."""
        if not self.tail:
            return None
        value = self.tail.value
        self.delete(self.tail)
        return value

    def move_to_front(self, node):
        """Removes the input node from its current spot in the
        List and inserts it as the new head node of the List."""
        self.delete(node)
        self.add_to_head(node.value)

    def move_to_end(self, node):
        """Removes the input node from its current spot in the
        List and inserts it as the new tail node of the List."""
        self.delete(node)
        self.add_to_tail(node.value)

    def delete(self, node):
        """Removes a node from the list and handles cases where
        the node was the head or the tail"""
        # if empty linked list
        if self.head == self.tail:
            self.head = self.tail = None
        elif node == self.head:
            self.head = self.head.next
            node.delete()
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()
        elif self.head is None or self.tail is None:
            print(f"\nhead: {self.head} and tail: {self.tail}")
            print("ERROR: Attempted to delete node from empty list")
            return
        else:
            node.delete()

        self.length -= 1