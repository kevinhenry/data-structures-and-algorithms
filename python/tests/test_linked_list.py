from code_challenges.linked_list.linked_list import LinkedList, Node, zip_lists


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


def test_empty_ll():
    ll = LinkedList()
    assert ll


def insert_one():
    ll = LinkedList()
    ll.insert("apples")
    actual = ll.head.value
    expected = "apples"
    assert actual == expected


def pointer():
    ll = LinkedList()
    ll.insert("a")
    ll.insert("b")
    ll.insert("c")
    actual = ll.head.value
    expected = "c"
    assert actual == expected


def true_search():
    ll = LinkedList(Node("apples", Node("oranges", Node("bananas", Node("cherry")))))
    actual = ll.includes("cherry")
    expected = True
    assert actual == expected


def false_search():
    ll = LinkedList(Node("apples", Node("oranges", Node("bananas", Node("cherry")))))
    actual = ll.includes("watermellon")
    expected = False
    assert actual == expected


def test_can_successfully_add_a_node_to_the_end_of_the_list():
    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")
    ll1.append("Z")
    expected = ["d", "c", "b", "a", "Z"]
    current = ll1.head
    index = 0
    while current is not None:
        assert current.value == expected[index]
        index += 1
        current = current.next


def test_can_successfully_add_muliple_nodes_to_the_end_of_list():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d")
    expected = ["a", "b", "c", "d"]
    current = ll1.head
    index = 0
    while current is not None:
        assert current.value == expected[index]
        index += 1
        current = current.next


def tests_can_successfully_insert_a_node_before_a_node_in_middle_of_list():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d")
    ll1.insert_before("c", "Z")
    expected = ["a", "b", "Z", "c", "d"]
    current = ll1.head
    index = 0
    while current is not None:
        assert current.value == expected[index]
        index += 1
        current = current.next


def test_Where_k_is_greater_than_the_length_of_the_linked_list():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d").append("e")

    actual = ll1.kth_from_the_end(2)
    expected = "c"
    assert actual == expected


def test_Where_k_and_the_length_of_the_list_are_the_same():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d").append("e")

    actual = ll1.kth_from_the_end(5)
    expected = "a"
    assert actual == expected


def test_Where_k_is_not_a_positive_integer():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d").append("e")

    actual = ll1.kth_from_the_end(-5)
    expected = "K is negative"
    assert actual == expected


def test_Where_the_linked_list_is_of_a_size_1():
    ll1 = LinkedList()
    ll1.append("a")

    actual = ll1.kth_from_the_end(1)
    expected = "a"
    assert actual == expected


def test_Happy_Path_where_k_is_not_at_the_end_but_somewhere_in_the_middle_of_the_linked_list():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d").append("e")

    actual = ll1.kth_from_the_end(3)
    expected = "b"
    assert actual == expected


def test_zip_lists():
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(2)
    ll2.append(5)
    ll2.append(9)
    ll2.append(4)
    zipped_list = zip_lists(ll1, ll2)
    actual = str(zipped_list)
    expected = "{1} -> {5} -> {3} -> {9} -> {2} -> {4} ->  None "
    assert actual == expected
