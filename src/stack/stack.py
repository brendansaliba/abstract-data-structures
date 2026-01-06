class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return not self.top

    def push(self, data):
        n = Node(data)
        if not self.is_empty():
            n.next = self.top
            self.top = n
        else:
            self.top = n
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        else:
            data = self.top.data
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            self.size -= 1
            return data
        
    def peek(self):
        if self.top:
            return self.top.data
        else:
            raise IndexError('Peek on empty stack')


if __name__ == "__main__":
    s = Stack()
    s.push('item 0')
    s.push('item 1')
    s.push('item 2')
    s.push('item 3')
    print(s.peek())
    s.pop()
    s.pop()
    s.pop()
    s.pop()

    current = s.top
    while current:
        print(current.data)
        current = current.next

    
