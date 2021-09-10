from code_challenges.linked_list.linked_list import LinkedList  # DANGER: user YOURS


class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self.buckets = [None] * self.size

    def add(self, key, value):
        index = self.hash(key)
        if not self.buckets[index]:
            self.buckets[index] = LinkedList()

        bucket = self.buckets[index]
        bucket.insert([key, value])

    def get(self, key):
        index = self.hash(key)
        if self.buckets[index] is None:
            return None

        current = self.buckets[index].head

        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next

        return None

    def contains(self, key):
        index = self.hash(key)
        if self.buckets[index] is None:
            return False

        current = self.buckets[index].head

        while current:
            if current.value[0] == key:
                return True
            current = current.next
        return False

    def hash(self, key):
        index = 0
        for char in key:
            index += ord(char)

        index *= 599

        index = index % self.size

        return index
