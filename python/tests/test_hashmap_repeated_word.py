from code_challenges.hashmap_repeated_word.hashmap_repeated_word import repeat_checker
from code_challenges.hashtable.hashtable import Hashtable
import pytest


# @pytest.mark.parametrize(
#     "test_string,hashtable,expected",
#     [
#         ("Once upon a time, there was a brave princess who...", Hashtable(), "a"),
#         (
#             "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...",
#             Hashtable(),
#             "it",
#         ),
#         (
#             "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...",
#             Hashtable(),
#             "summer",
#         ),
#     ],
# )
# def test_repeated_word(test_string, hashtable, expected):
#     actual = repeat_checker(test_string, hashtable)
#     assert actual == expected


def test_can_instantiate_a_hashamp():
    hashmap = Hashtable()
    assert hashmap


def test_empty_string_returns_None():
    word_list = " "
    actual = repeat_checker(word_list)
    assert actual == None


def test_no_repeats_returns_None():
    word_list = "aa bb cc ddd ee fff"
    actual = repeat_checker(word_list)
    assert actual == None


def test_will_return_first_repeated_word():
    word_list = "aa DDD aA cc ddd ee fff"
    actual = repeat_checker(word_list)
    assert actual == "aa"


def test_function_ignores_upper_and_lower_case():
    word_list = "aa DDD bb cc ddd ee fff"
    actual = repeat_checker(word_list)
    assert actual == "ddd"


def test_will_not_include_punctuations_in_check():
    word_list = "aa DDD bb cc ddd ee fff !DdD,"
    actual = repeat_checker(word_list)
    assert actual == "ddd"
