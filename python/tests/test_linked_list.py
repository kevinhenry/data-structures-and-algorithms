from linked_list.linked_list import LinkedList, Node


def test_node_instance():
    node = Node("apples", None)
    actual = node.value
    expected = "apples"
    assert actual == expected
    assert node.next == None


def test_two_nodes():
    node2 = Node("orange", None)
    node1 = Node("apples", node2)
    actual = node1.next.value
    expected = "orange"
    assert actual == expected


# def test_detect():
#     actual = LinkedList(includes)
#     expected = True
#     assert actual == expected


def test_empty_ll():
    ll = LinkedList()
    assert ll
