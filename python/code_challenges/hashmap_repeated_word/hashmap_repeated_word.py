from code_challenges.linked_list.linked_list import LinkedList
import re


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


# class Hashtable:
#     def __init__(self, size=1024):
#         self._size = size
#         self._buckets = size * [None]

#     def add(self, key, value):
#         index = self._hash(key)
#         if not self._buckets[index]:
#             self._buckets[index] = LinkedList()

#         self.buckets[index].append((key, value))

#     def get(self, key):
#         request_key = self._hash(key)
#         if self._buckets[request_key]:
#             current = self._buckets[request_key].head
#             while current:
#                 if current.data[0] == key:
#                     return current.data[1]
#                 current = current.next
#         else:
#             return None

#     def contains(self, key):
#         request_key = self._hash(key)
#         if self._buckets[request_key]:
#             current = self._buckets[request_key].head
#             while current:
#                 if current.data[0] == key:
#                     return True
#                 current = current.next
#         else:
#             return False

#     def _hash(self, key):
#         sum = 0
#         for char in key:
#             sum += ord(char)

#         product = sum * 599
#         index = product % self._size
#         return index


def repeat_checker(str):
    if len(str) == 0:
        return None

    hashmap = Hashtable()
    lowered = str.lower()
    word_list = re.findall(r"\w+", lowered)

    for word in word_list:
        if hashmap.contains(word):
            return word
        else:
            hashmap.add(word, word)

    return None


# def repeat_checker(string, hashtable):
#     string = string.casefold()
#     word_list = string.split(" ")
#     for i, item in enumerate(word_list):
#         if not item.isalpha():
#             word_list[i] = [char for char in item if char.isalpha()]
#             word_list[i] = "".join(word_list[i])
#         if not len(word_list[i]):
#             word_list.pop(i)

#     print(word_list)

#     for word in word_list:
#         if hashtable.contains(word):
#             return word
#         hashtable.add(word, word)

#     return None


# if __name__ == "__main__":

#     test_hashtable = Hashtable()

#     test_string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
#     repeted_word = repeat_checker(test_string, test_hashtable)
#     print(repeted_word)
