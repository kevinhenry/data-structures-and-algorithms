# from code_challenges.tree.tree import BinarySearchTree

from code_challenges.stack_and_queue.stack_and_queue import Queue

def breadth_first(tree):
    values_list = []
    queue = Queue()

    queue.enqueue(tree)
    while queue:
        front = queue.dequeue()
        if front == None:
            continue
        values_list.append(front.root)
        queue.enqueue(front.left_child)
        queue.enqueue(front.right_child)

    return values_list
