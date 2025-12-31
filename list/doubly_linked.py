class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
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
        for n in self.iter():
            if n.data == data:
                return True
        return False
            
    def prepend(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def append(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert_at_index(self, data, index):
        current = self.head
        prev = self.head
        node = Node(data)
        count = 0
        while current:
            if index == 0:
                current.prev = node
                node.next = current
                self.head = node
                self.size += 1
                return
            elif count == index:
                current.prev = node
                node.next = current
                node.prev = prev
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
                if current is self.head:
                    node.next = current
                    node.next.prev = node
                    self.head = node
                else:
                    node.prev = prev
                    node.next = current
                    node.next.prev = node
                    prev.next = node
                self.size += 1
                return
            prev = current
            current = current.next
        print('The target does not exist in the list')

    def insert_after_target(self, data, target):
        current = self.head
        prev = self.head
        node = Node(data)
        while current:
            if current.data == target:
                if current.next is None:
                    node.prev = current
                    node.prev.next = node
                else: 
                    node.prev = current
                    node.next = current.next
                    node.prev.next = node
                    node.next.prev = node
                self.size += 1
                return
            prev = current
            current = current.next

    def delete(self, data):
        current = self.head
        deleted = False
        if current is None:
            print('List is empty')
        elif current.data == data:
            self.head.next.prev = None
            self.head = current.next
            deleted = True
            print(f'Deleted {data}') 
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            deleted = True
            print(f'Deleted {data}')
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    deleted = True
                if not deleted:
                    print('Item not found in list')
        if deleted:
            self.size -= 1