class InvalidOperationError(BaseException):
    pass


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self, node=None):
        self.top = node

    def push(self, value):
        # create a node from value
        node = Node(value)
        # point new node to top of stack
        node.next = self.top
        # assign node to top of stack
        self.top = node

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        node = self.top
        self.top = self.top.next
        return node.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False


class Queue:
    # FirstInFirstOut
    def __init__(self, node=None):
        self.front = node
        self.rear = node

    def enqueue(self, value):
        node = Node(value)

        if self.front is None:
            self.front = node
            self.rear = node
            return self

        self.rear.next = node
        self.rear = node
        return self

    def dequeue(self):

        if self.front is None:
            return None

        dequed = self.front.value
        self.front = self.front.next
        return dequed

    def peek(self):

        if self.front is None:
            return None

        return self.front.value

    def isEmpty(self):
        return self.front == None


if __name__ == "__main__":
    pass
