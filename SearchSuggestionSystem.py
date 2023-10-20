"""
https://leetcode.com/problems/search-suggestions-system/description/

You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with searchWord.
If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

"""
from bisect import bisect_left
from typing import List


# Time Complexity  : O(nlogn + n + m)
# Space Complexity  : O(N)
# Two Pointer Approach
def searchSuggestion2Pointer(products, search_word):
    result = []
    # Sorting first for lexicographical order
    products.sort()
    pointer1, pointer2 = 0, len(products) - 1
    for x in range(len(search_word)):
        char = search_word[x]
        while pointer1 <= pointer2 and (len(products[pointer1]) <= x or products[pointer1][x] != char):
            pointer1 += 1
        while pointer1 <= pointer2 and (len(products[pointer2]) <= x or products[pointer2][x] != char):
            pointer2 -= 1
        result.append([])  # Appending empty list
        remain_element = pointer2 - pointer1 + 1
        for y in range(min(3, remain_element)):
            result[-1].append(products[pointer1 + y])  # result[-1] returns last element
    print(result)
    return result


products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
searchSuggestion2Pointer(products, searchWord)


# Time - O(nlogn + mlogn) - Sorting requires O(nlogn) and O(logn) is for binary search the products for a prefix.
# Space - O(1)
def searchSuggestionBinary(product, search_word):
    product.sort()
    prefix = ''
    res = []
    i = 0
    for c in searchWord:
        prefix += c
        i = bisect_left(products, prefix, i)  # Binary Search
        res.append([word for word in products[i:i + 3] if word.startswith(prefix)])
    return res


product = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
searchSuggestion2Pointer(product, searchWord)


# Using Tree
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = list()
        self.n = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children: node.children[c] = TrieNode()
            node = node.children[c]
            if node.n < 3:
                node.words.append(word)
                node.n += 1

    def find_word_by_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children: return ''
            node = node.children[c]
        return node.words


class Solution:
    def suggestedProducts(self, A: List[str], searchWord: str) -> List[List[str]]:
        A.sort()
        trie = Trie()
        for word in A: trie.add_word(word)
        ans, cur = [], ''
        for c in searchWord:
            cur += c
            ans.append(trie.find_word_by_prefix(cur))
        return ans
