import pytest
from code_challenges.tree.tree import Node, BinarySearchTree, BinaryTree

# @pytest.mark.skip("pending")
def test_node_has_value():
    node = Node("apple")
    assert node.value == "apple"


# @pytest.mark.skip("pending")
def test_node_has_left_of_none():
    node = Node("apple")
    assert node.left is None


# @pytest.mark.skip("pending")
def test_node_has_right_of_none():
    node = Node("apple")
    assert node.right is None


# @pytest.mark.skip("pending")
def test_create_binary_tree():
    tree = BinaryTree()
    assert tree


# @pytest.mark.skip("pending")
def test_binary_tree_has_root():
    tree = BinaryTree()
    assert tree.root is None


# @pytest.mark.skip("pending")
def test_create_binary_search_tree():
    tree = BinarySearchTree()
    assert tree


def test_empty_tree():
    tree = BinaryTree(Node())
    actual = tree.root.value
    expected = None
    assert actual == expected


def test_one_root_on_tree():
    tree = BinaryTree(Node())
    actual = tree.root.value
    expected = None
    assert actual == expected


def test_add_left_and_right_node():
    tree = BinarySearchTree()
    tree.add(3)
    actual = tree.root.value
    expected = 3
    assert actual == expected


def test_pre_order_traversal():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(4)
    tree.root.right = Node(2)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(5)
    actual = tree.pre_order()
    expected = [1, 4, 3, 5, 2]
    assert actual == expected


def test_in_order_traversal():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    actual = tree.in_order()
    expected = [4, 2, 5, 1, 3]
    assert actual == expected


def test_post_order_traversal():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    actual = tree.post_order()
    expected = [4, 5, 2, 3, 1]
    assert actual == expected


def test_finding_maximum_value():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(9)
    tree.root.left.right = Node(12)
    tree.root.left.right.left = Node(1)
    tree.root.left.right.right = Node(3)
    tree.root.right.right = Node(8)
    tree.root.right.left = Node(10)
    actual = tree.find_maximum_value()
    expected = 12
    assert actual == expected
