import pytest
from code_challenges.stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter, Node


def test_enqueue():
    a = AnimalShelter()
    a.enqueue("dog")
    actual = a.front.value
    expected = "dog"
    assert actual == expected


def test_dequeue():
    a = AnimalShelter()
    a.enqueue("cat")
    actual = a.dequeue("cat")
    expected = "cat"
    assert actual == expected


def test_dequeue_when_pref_is_not_dog_or_cat():
    a = AnimalShelter()
    a.enqueue("cat")
    a.enqueue("dog")
    actual = a.dequeue("bunny")
    expected = "null"
    assert actual == expected
