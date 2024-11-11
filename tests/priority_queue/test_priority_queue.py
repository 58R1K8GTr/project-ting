from ting_file_management.priority_queue import PriorityQueue
from pytest import raises


def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
    priority_queue = PriorityQueue()
    assert len(priority_queue) == 0
    mocks = list(map(lambda x: {'qtd_linhas': x}, (1, 6, 3)))
    for count, mock in enumerate(mocks, 1):
        priority_queue.enqueue(mock)
        assert len(priority_queue) == count
    assert priority_queue.search(1) == mocks[2]
    with raises(IndexError):
        priority_queue.search(5)
    assert priority_queue.dequeue() == mocks[0]
    assert priority_queue.dequeue() == mocks[2]
    assert priority_queue.dequeue() == mocks[1]
