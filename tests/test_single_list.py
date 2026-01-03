from src.list.singly_linked import SinglyLinkedList

def test_list_empty_on_creation():
    l = SinglyLinkedList()
    assert l.is_empty()
    assert l.size == 0

def test_append():
    l = SinglyLinkedList()
    l.append('item 0')
    assert l.head.data == 'item 0'
    assert l.size == 1