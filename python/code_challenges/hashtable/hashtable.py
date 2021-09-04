from code_challenges.linked_list.linked_list import LinkedList  # DANGER: user YOURS


class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self.buckes = [None] * self.size

    def hash(self, key):
        sum = 0
        for char in key:
            numeric_value = ord(char)
            sum += numeric_value

        product = sum * 599

        index = product % self.size

        return index

    def add(self, key, value):

        index = self.hash(key)

        if not self.buckets[index]:
            self.buckets[index] = LinkedList()

        bucket = self.buckets[index]

        bucket.insert([key, value])
