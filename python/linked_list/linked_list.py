class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)

        if self.head is not None:
            node.next = self.head  # pear -> orange
            self.head = node  # HEAD: pear -> orange

    def includes(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    #

    #     node = node.next:

    # return False

    # pph

    # computational thinking. takes a massive problem and seperates it down into small little challenges = litte wins.

    # get into the habbit of is doing the write out.

    # ll2.head.value = pear
    # ll2.head.next = orange
    # ll2.head.next.next = apple

    # ll2 pears -> orange -> apple -> None

    # current = 112.head
    # while current.value  is not None:
    #     # do something
    #     current = current.next

    # if __name__ == "__main__":
    #     ll2 = LinkedList()
    #     ll2.insert('apples')
    #     ll2.insert('orange')
    #     ll2.insert('pears')

    # function link list head -> apples? / mope -> apples yet? / nope -> apples yet? / true
    # if linked list's value becomes none, That is the end of the linked list.

    # while loop - if value is in the linked list, return items, if not ten return None

    # ll = LinkedList()
    # node1 = Node("apples")
    # node2 = Node("orange")
    # node3 = Node("pear")
    # ll.head == node1
    # node1.next == node2
    # node2.next == node3

    # node1.next == None

    # llhead = apple -> 'orange' -> 'pear' -> None

    # ll1 = LinkedList(Node("apples", Node("orange", Node("pear"))))

    # llhead = apples -> 'orange' -> 'pear' -> None
    # ll1.next = None
