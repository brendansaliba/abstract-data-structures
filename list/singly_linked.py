class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def iter(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def contains(self, data):
        for d in self.iter():
            if d == data:
                return True
        return False

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def insert_at_index(self, data, index):
        current = self.head
        prev = self.head
        node = Node(data)
        count = 0
        while current:
            if index == 0:
                node.next = current
                self.head = node
                self.size += 1
                return
            elif count == index:
                node.next = current
                prev.next = node
                self.size += 1
                return
            count += 1
            prev = current
            current = current.next
        if count <= index:
            print('Target index does not yet exist. Please use the append() method to append to the end of the list.')

    def insert_before_target(self, data, target):
        current = self.head
        prev = self.head
        node = Node(data)
        while current:
            if current.data == target:
                node.next = current
                prev.next = node
                self.size += 1
                return
            prev = current
            current = current.next

    def insert_after_target(self, data, target):
        current = self.head
        prev = self.head
        node = Node(data)
        while current:
            if current.data == target:
                node.prev = current
                node.next = current.next
                if current.next is None:
                    self.tail = node
                current.next = node
                self.size += 1
                return
            prev = current
            current = current.next

    def delete_first_node(self):
        if self.head is None:
            print('The list is empty')
            return
        self.head = self.head.next
        self.size -= 1

    def delete_last_node(self):
        if self.tail is None:
            print('The list is empty')
            return
        current = self.head
        prev = self.head
        if current.next is None:
            self.clear()
            return
        while current:
            if current.next is None:
                prev.next = None
                self.tail = prev
                self.size -= 1
                return
            prev = current
            current = current.next

    def delete(self, data):
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current is self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0