from src.queue.queue import Queue

def test_queue_empty_on_creation():
    q = Queue()
    assert q.size == 0