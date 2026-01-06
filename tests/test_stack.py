from src.stack.stack import Stack

def test_stack_empty_on_creation():
    s = Stack()
    assert s.size == 0