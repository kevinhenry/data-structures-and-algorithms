import pytest

from code_challenges.stack_and_queue.stack_and_queue import Node, Stack


def test_push_onto_empty():
    s = Stack()
    s.push("a")
    actual = s.top.value
    expected = "a"
    assert actual == expected


def test_push_onto_full():
    s = Stack()
    s.push("a")
    s.push("b")
    s.push("c")
    actual = s.top.value
    expected = "c"
    assert actual == expected


def test_pop_single():
    s = Stack()
    s.push("a")
    actual = s.pop()
    expected = "a"
    assert actual == expected


def test_pop_some():
    s = Stack()
    s.push("a")
    s.push("b")
    s.push("c")
    s.pop()
    actual = s.pop()
    expected = "b"
    assert actual == expected


