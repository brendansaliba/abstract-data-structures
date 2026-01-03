class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class CircularList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def iter(self): # Will loop through once only
        count = 0
        current = self.head
        while count < self.size and current:
            yield current
            current = current.next
            count += 1

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
            node.next = self.head
        else:
            self.head = node
            self.tail = node
            self.tail.next = self.head
        self.size += 1

    def delete(self, data):
        current = self.head
        prev = self.head

        while current:
            if current.data == data:
                if current is self.head:
                    self.head.next.prev = self.tail
                    self.head = self.head.next
                    self.tail.next = self.head
                elif current is self.tail:
                    prev.next = self.head
                    self.head.prev = prev
                    self.tail = prev
                else:
                    prev.next = current.next
                self.size -= 1
                return
            if current is self.tail:
                break
            prev = current
            current = current.next
            
        print("Item is not in the list")

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0