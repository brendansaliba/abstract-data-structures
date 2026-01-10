class Node():
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next: Node = next
        self.prev: Node = prev

class Queue():
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size: int = 0

    def iter(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

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

    def dequeue(self):
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
        elif self.size > 1:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
        else:
            print("Queue is empty")

if __name__ == "__main__":
    q = Queue()
    q.enqueue("item 1")
    q.enqueue("item 2")
    q.enqueue("item 3")
  
    for n in q.iter():
        print(n.data)