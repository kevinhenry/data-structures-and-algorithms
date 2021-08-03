from code_challenges.tree_fizz_buzz.tree_fizz_buzz import Node, K_aryTree, fizz_buzz_tree
import pytest


def test_empty_tree():
    tree = K_aryTree(Node())
    actual = fizz_buzz_tree(tree)
    expected = "Empty"
    assert actual == expected


def test_tree_traverse():
    tree = K_aryTree(Node(1))
    tree.root.left = Node(4)
    tree.root.right = Node(8)
    tree.root.left.left = Node(15)
    tree.root.left.right = Node(85)
    tree.root.right.left = Node(42)
    actual = fizz_buzz_tree(tree)
    expected = [1, 4, "FizzBuzz", "Buzz", 8, "Fizz"]
    assert actual == expected
