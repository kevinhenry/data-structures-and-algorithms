import pytest

from code_challenges.stack_and_queue.stack_and_queue import Node, Stack, Queue, InvalidOperationError


def test_successfully_push_onto_a_stack():
    stack = Stack()
    stack.push("a")
    actual = stack.top.value
    expected = "a"
    assert actual == expected


def test_successfuly_push_mult_values_onto_a_stack():
    stack = Stack()
    stack.push("a")
    stack.push("b")
    stack.push("c")
    actual = stack.top.value
    expected = "c"
    assert actual == expected


def test_succ_pop_off_stack():
    stack = Stack()
    stack.push("a")
    actual = stack.pop()
    expected = "a"
    assert actual == expected


def test_succ_empty_stack_after_mult_pops():
    stack = Stack()
    stack.push("a")
    stack.push("b")
    stack.push("c")
    stack.pop()
    actual = stack.pop()
    expected = "b"
    assert actual == expected


def test_succ_peek_next_item_stack():
    stack = Stack()
    stack.push("a")
    stack.push("b")
    actual = stack.peek()
    expected = "b"
    assert actual == expected


def test_succ_instantiate_an_empty_stack():
    stack = Stack()
    stack.push("a")
    stack.push("b")
    stack.push("c")
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.is_empty()
    expected = True
    assert actual == expected


def test_calling_pop_or_peek_empty_stack_raises_exception():
    stack = Stack()
    with pytest.raises(InvalidOperationError) as e:
        stack.pop()
    assert str(e.value) == "Method not allowed on empty collection"


def test_succ_enqueue_into_queue():
    queue = Queue()
    queue.enqueue("a")
    assert queue.front.value == "a"


def test_succ_enqueue_multiple_values_into_queue():
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    queue.enqueue("d")
    assert queue.front.value == "a"
    assert queue.rear.value == "d"


def test_succ_dequeue_out_of_queue_expected_value():
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    queue.enqueue("d")
    actual = queue.dequeue()
    expected = "a"
    assert actual == expected


def test_succ_peek_into_a_queue_seeing_the_exected_value():
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    queue.enqueue("d")
    actual = queue.peek()
    expected = "a"
    assert actual == expected


def test_succ_empty_queue_after_multiple_dequeues():
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    queue.enqueue("d")

    while queue.peek():
        queue.dequeue()

    assert queue.front == None


def test_succ_instantiate_empty_queue():
    queue = Queue()
    assert queue.front == None
    assert queue.rear == None


def test_calling_dequeue_or_peek_on_empty_queue_raises_exception():
    queue = Queue()
    assert queue.dequeue() == None
