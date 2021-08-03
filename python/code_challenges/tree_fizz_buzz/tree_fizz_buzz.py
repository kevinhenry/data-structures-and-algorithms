class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class K_aryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        pre_order_list = []

        def traverse(root):
            if root is None:
                return "Empty"

            pre_order_list.append(root.value)
            traverse(root.left)
            traverse(root.right)

        traverse(self.root)
        return pre_order_list


def fizz_buzz_tree(tree):
    root = tree.root
    tree_list = []
    if root.value is None:
        return "Empty"

    def traverse(root):
        if root is None:
            return
        if root.value % 3 == 0 and root.value % 5 == 0:
            root.value = "FizzBuzz"
        elif root.value % 3 == 0:
            root.value = "Fizz"
        elif root.value % 5 == 0:
            root.value = "Buzz"

        tree_list.append(root.value)
        traverse(root.left)
        traverse(root.right)

    traverse(root)

    return tree_list


if __name__ == "__main__":
    tree = K_aryTree(Node(1))
    tree.root.left = Node(4)
    tree.root.right = Node(8)
    tree.root.left.left = Node(15)
    tree.root.left.right = Node(85)
    tree.root.right.left = Node(42)

    tree = K_aryTree(Node())
    print(fizz_buzz_tree(tree))
