"""
Given an array of strings 'arr', group the anagrams together.

Input: arr = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""
from typing import List


def anagrams(arr):
    dict = {}
    for word in arr:
        sort_word = "".join(sorted(word))
        if sort_word in dict:
            dict[sort_word].append(word)

        else:
            dict[sort_word] = [word]
    return List[dict.values()]


arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams(arr)
