class Node():
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        n = Node(data=data)
        if self.head == None:
            self.head = n
            self.tail = self.head
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
        self.size += 1
