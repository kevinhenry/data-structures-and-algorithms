import pytest

from stack_and_queue import Node, Stack, Queue, InvalidOperationError

# test_empty_node
def test_inst_empty_node():
    new_node = Node()
    # actual = node.value
    # expected = None
    # assert actual == expected
    assert new_node


# test node single value
def node_single_value():
    new_node = Node(5)
    actual = new_node.value
    expected = 5
    assert actual == expected


# test node does not = a diff value
def test_value():
    new_node = Node(5)
    actual = new_node.value
    expected = 6
    assert actual != expected


# create node that value and next - make sure next is expected
def test_next_value():
    new_node = Node(5, Node(6))
    actual = new_node.next.value
    expected = 6
    assert actual == expected


def test_successfully_push_onto_a_stack():
    stack = Stack()
    stack.push("a")
    actual = stack.top.value
    expected = "a"
    assert actual == expected


def test_successfuly_push_mult_values_onto_a_stack():
    stack = Stack()
    stack.push("a")
    stack.push("b")
    stack.push("c")
    actual = stack.top.value
    expected = "c"
    assert actual == expected


def test_succ_pop_off_stack():
    stack = Stack()
    stack.push("a")
    actual = stack.pop()
    expected = "a"
    assert actual == expected


def test_succ_empty_stack_after_mult_pops():
    stack = Stack()
    stack.push("a")
    stack.push("b")
    stack.push("c")
    stack.pop()
    actual = stack.pop()
    expected = "b"
    assert actual == expected


# def test_succ_empty_stack_after_mult_pops(create_stack):
#     s = create_stack
#     s.push(1)
#     # 1 is top
#     s.push(2)
#     # 1 is bottom 2 is top
#     s.push(3)
#     # 1 bottom 2 is middle 3 is top
#     s.pop()
#     # pop 3 off top, 2 new top
#     s.pop()
#     # pop 2 off top, 1 new top
#     actual = s.head.value
#     expected = 1
#     assert actual == expected


def test_succ_peek_next_item_stack():
    stack = Stack()
    stack.push("a")
    stack.push("b")
    actual = stack.peek()
    expected = "b"
    assert actual == expected


def test_succ_instantiate_an_empty_stack():
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


# create a new test insta an empty stack and make sure it exists
def test_empty_stack():
    new_stack = Stack()
    assert new_stack


# create a stack and a node, create stack with a node, test the node is at top of stack
def test_has_a_value():
    new_stack = Stack()
    new_stack.push("a")
    actual = new_stack.top.value
    expected = "a"
    assert actual == expected


def test_calling_pop_or_peek_empty_stack_raises_exception():
    stack = Stack()
    with pytest.raises(InvalidOperationError) as e:
        stack.pop()
    assert str(e.value) == "Method not allowed on empty collection"


def test_succ_enqueue_into_queue():
    queue = Queue()
    queue.enqueue("a")
    assert queue.front.value == "a"


def test_succ_enqueue_multiple_values_into_queue():
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    queue.enqueue("d")
    assert queue.front.value == "a"
    assert queue.rear.value == "d"


def test_succ_dequeue_out_of_queue_expected_value():
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    queue.enqueue("d")
    actual = queue.dequeue()
    expected = "a"
    assert actual == expected


def test_succ_peek_into_a_queue_seeing_the_exected_value():
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    queue.enqueue("d")
    actual = queue.peek()
    expected = "a"
    assert actual == expected


def test_succ_empty_queue_after_multiple_dequeues():
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    queue.enqueue("d")

    while queue.peek():
        queue.dequeue()

    assert queue.front == None


def test_succ_instantiate_empty_queue():
    queue = Queue()
    assert queue.front == None
    assert queue.rear == None


def test_calling_dequeue_or_peek_on_empty_queue_raises_exception():
    queue = Queue()
    assert queue.dequeue() == None
