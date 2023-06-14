"""
https://practice.geeksforgeeks.org/problems/word-break1352/1

Given a string A and a dictionary of n words B, find out if A can be segmented into a space-separated sequence of dictionary words.

Note: From the dictionary B each word can be taken any number of times and in any order.
Example 1:

Input:
n = 12
B = { "i", "like", "sam",
"sung", "samsung", "mobile",
"ice","cream", "icecream",
"man", "go", "mango" }
A = "ilike"
Output:
1
Explanation:
The string can be segmented as "i like".


Example 2:

Input:
n = 12
B = { "i", "like", "sam",
"sung", "samsung", "mobile",
"ice","cream", "icecream",
"man", "go", "mango" }
A = "ilikesamsung"
Output:
1
Explanation:
The string can be segmented as
"i like samsung" or "i like sam sung".

Expected time complexity: O(s2)

Expected auxiliary space: O(s) , where s = length of string A
"""


def wordBreakDP(given_string, given_dictionary):
    # dp_arr initialized to all FALSE
    dp_arr = [False] * (len(given_string) + 1)
    # Setting to True as a Base case
    dp_arr[0] = True
    # This loop will be ahead of inner loop
    for x in range(1, len(given_string) + 1):
        # this loop will start at input_string[0] and increment up to x
        # Checking each time if input_string[y:x] matches in input_dictionary
        for y in range(x):
            # dp_arr[y] tells us if we have successfully created a word up to that index.
            # Checking dp_arr[y] helps us ensure that we're only marking tracker True when words are adjacent.
            if dp_arr[y] and given_string[y:x] in given_dictionary:
                dp_arr[x] = True
                break  # control goes to outer loop to increment x
    return dp_arr[-1]


input_dictionary = {"i", "like", "sam",
                    "sung", "samsung", "mobile",
                    "ice", "cream", "icecream",
                    "man", "go", "mango"}
input_string = "ilikesamsung"

print("We can able to break the word : ", wordBreakDP(input_string, input_dictionary))
# We can break the word :  True


def wordBreakDPAnother(given_string, given_dictionary):
    # dp_array initialized to all FALSE
    dp_array = [False] * (len(given_string) + 1)
    # Setting to True as a Base case
    dp_array[0] = True
    for x in range(1, len(given_string) + 1):
        # check each word in wordDict rather than iterating from 0 to i
        for word in given_dictionary:
            if len(word) > x:
                continue
            if given_string[x - len(word):x] == word and dp_array[x - len(word)]:
                dp_array[x] = dp_array[x - len(word)]
                break
    return dp_array[len(given_string)]


input_dictionary = {"i", "like", "sam",
                    "sung", "samsung", "mobile",
                    "ice", "cream", "icecream",
                    "man", "go", "mango"}
input_string = "ilikesamsung"
print("We can able to break the word : ", wordBreakDPAnother(input_string, input_dictionary))
