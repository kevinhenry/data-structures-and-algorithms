import pytest
from code_challenges.quick_sort.quick_sort import quick_sort


def test_sort_output():
    sort_list = [8, 4, 23, 42, 16, 15]
    actual = quick_sort(sort_list, 0, 5)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_not_sort_output():
    sort_list = [8, 4, 23, 42, 16, 15]
    actual = quick_sort(sort_list, 0, 5)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual != expected
