from code_challenges.tree.tree import BinarySearchTree
from code_challenges.stack_and_queue.stack_and_queue import Queue
from tree_breadth_first.tree_breadth_first import breadth_first
import pytest


def test_breadth_first():
    my_tree = BinarySearchTree()
    values_list = [17, 1738, 52, 16, 6, 888]
    for number in values_list:
        my_tree.add(number)
    actual = breadth_first(my_tree)
    expected = [17, 16, 1738, 6, 52, 888]
    assert actual == expected


##########
# Fixtures
##########


@pytest.fixture
def my_tree():
    my_tree = BinarySearchTree()
    values_list = [17, 1738, 52, 16, 6, 888]
    for number in values_list:
        my_tree.add(number)
    return my_tree

    @pytest.fixture(autouse=True)
    def clean():
        my_tree = None
