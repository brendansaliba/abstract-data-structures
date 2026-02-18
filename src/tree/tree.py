class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    
class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def insert(self, data):
        n = Node(data)

        if self.root is None:
            self.root = n
            return self.root
        else:
            current = self.root
            parent = None

            while True:
                if current.left is None and current.right is None:
                    current.left = n
                    return current.left
                elif current.left is not None and current.right is None:
                    current.right = n
                    return current.right
                elif current.left is not None and current.right is not None:
                    parent = current
                    current = current.left
    
    def traverse(self, n: Node = None):
        if self.root is None:
            print("Tree is empty.")
            return

        if n is None:
            return
        
        print(n.data)
        self.traverse(n.left)
        self.traverse(n.right)


if __name__ == "__main__":
    t = Tree()
    t.insert("one")
    t.insert("two")
    t.insert("three")
    t.insert("four")

    t.traverse(t.root)