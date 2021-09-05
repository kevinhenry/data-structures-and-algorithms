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
        request_key = self.hash(key)
        if self.buckets[request_key]:
            current = self.buckets[request_key].head
            while current:
                if current.data[0] == key:
                    return current.data[1]
                current = current.next
        else:
            return None

    def contains(self, key):
        request_key = self.hash(key)
        if self.buckets[request_key]:
            current = self.buckets[request_key].head
            while current:
                if current.data[0] == key:
                    return True
                current = current.next
        else:
            return False

    def hash(self, key):
        sum = 0
        for char in key:
            numeric_value = ord(char)
            sum += numeric_value

        product = sum * 599

        index = product % self.size

        return index
