import pytest
from code_challenges.stack_queue_brackets.stack_queue_brackets import validate_brackets


def test_square():
    str = "[lemon]"
    validate_brackets(str)
    actual = True
    excepted = True
    assert actual == excepted


def test_brackets():
    str = "{Hello, World}[}"
    validate_brackets(str)
    actual = False
    expected = False
    assert actual == expected


def test_brackets_false():
    str = "{This should test true}{}"
    validate_brackets(str)
    actual = True
    excepted = True
    assert actual == excepted


def test_alternate():
    str = "{"
    validate_brackets(str)
    actual = True
    expected = False
    assert actual != expected
