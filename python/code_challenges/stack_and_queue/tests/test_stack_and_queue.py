import pytest

from python.code_challenges.stack_and_queue.stack_and_queue import Node, Stack,InvalidOperationError


def test_push_onto_empty():
    stack = Stack()
    stack.push("a")
    actual = stack.top.value
    expected = "a"
    assert actual == expected


def test_push_onto_full():
    stack = Stack()
    stack.push("a")
    stack.push("b")
    stack.push("c")
    actual = stack.top.value
    expected = "c"
    assert actual == expected


def test_pop_single():
    stack = Stack()
    stack.push("a")
    actual = stack.pop()
    expected = "a"
    assert actual == expected


def test_pop_some():
    stack = Stack()
    stack.push("a")
    stack.push("b")
    stack.push("c")
    stack.pop()
    actual = stack.pop()
    expected = "b"
    assert actual == expected


def test_check_not_empty():
    stack = Stack()
    stack.push("a")
    stack.push("b")
    actual = stack.is_empty()
    expected = False
    assert actual == expected


def test_pop_until_empty():
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


def test_peek():
    stack = Stack()
    stack.push("a")
    stack.push("b")
    actual = stack.peek()
    expected = "b"
    assert actual == expected


def test_peek_empty():
    stack = Stack()
    with pytest.raises(InvalidOperationError) as e:
        stack.peek()
    assert str(e.value) == "Method not allowed on empty collection"


def test_pop_empty():
    stack = Stack()
    with pytest.raises(InvalidOpertionError) as e:
        stack.pop()
    assert str(e.value) == "Method not allowed on empty collection"
