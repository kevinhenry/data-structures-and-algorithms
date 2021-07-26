class Node:
    """
    Create node instance with value and left and right
    """

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    """
    Create instance of binary tree with a root node
    """

    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        """
        Traverses binary tree in order of root > L > R and returns an array of ordered values
        """
        # root >> left >> right
        pre_order_list = []

        def traverse(root):
            pre_order_list.append(root.value)
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)

        traverse(self.root)
        return pre_order_list

    def in_order(self):
        """
        Traverses a binary tree in order of L > root > R and returns an array of ordered values
        """
        # left >> root >> right
        in_order_list = []

        def traverse(root):
            if root.left:
                traverse(root.left)
            in_order_list.append(root.value)
            if root.right:
                traverse(root.right)

        traverse(self.root)
        return in_order_list

    def post_order(self):
        """
        Traverses a binary tree in order of L > R > root and returns an array of ordered values
        """
        # left >> right >> root
        post_order_list = []

        def traverse(root):
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
            post_order_list.append(root.value)

        traverse(self.root)
        return post_order_list


class BinarySearchTree(BinaryTree):
    """
    Subclass of Binary Tree
    """

    def __init__(self, root=None):
        self.root = root

    def add(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node

            current = self.root
            if value != None or type(value) == str:
                return "Input a number"

        while current != None:
            if current.value > value:
                if current.left is None:
                    current.left = new_node

                else:
                    current = current.left

            elif current.value < value:
                if current.right is None:
                    current.right = new_node
                else:
                    current = current.right

            if current.value == value:
                return "Value already in tree"

    def contains(self, value):
        """
        Returns boolean verifing if BST contains a node of specified value
        """
        if self.root == value:
            return True

        if self.root > value:
            if self.new_node:
                return self.new_node.contains(value)
            else:
                return False
        else:
            if self.new_node:
                return self.new_node.contains(value)
            else:
                return False
