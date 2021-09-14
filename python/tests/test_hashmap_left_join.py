from code_challenges.hashmap_left_join.hashmap_left_join import left_join
import pytest


def test_function_will_account_for_empty_left(hashmap1):
    actual = left_join({}, hashmap1)
    expected = []
    assert actual == expected


def test_function_will_account_for_empty_right(hashmap1):
    actual = left_join(hashmap1, {})
    expected = []
    assert actual == expected


def test_function_will_account_for_both_empty():
    actual = left_join({}, {})
    expected = []
    assert actual == expected


@pytest.fixture
def hashmap1():
    obj = {"a": "aa", "b": "bb", "c": "cc", "d": "dd", "e": "ee"}
    return obj


@pytest.fixture
def hashmap2():
    obj = {"a": "aa", "b": "bb", "g": "gg", "h": "hh", "e": "ee"}
    return obj
