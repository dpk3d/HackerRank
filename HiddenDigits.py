"""
In this challenge you're given a random string containing hidden and visible digits. The digits are hidden
behind lower case latin letters as follows: 0 is behind 'a', 1 is behind 'b' etc., 9 is behind 'j'. Any
other symbol in the string means nothing and has to be ignored. So the challenge is to find all visible and
hidden digits in the string and print them out in order of their appearance.

INPUT:

Your program should read lines from standard input. Each line in this file contains a
string. You may assume that there will be no white spaces inside the string.
E.g.
1. abcdefghik

Output :

For each test case print out all visible and hidden digits in order of their appearance.
Print out NONE if no digits in the strings.
"""

import sys


def process(line):
    # Creating a Map of digits and letters
    digit_map = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9'}
    result = []
    # Looping thought the Map
    for x, char in enumerate(line):
        if digit_map.get(char, None):
            # If Character exists in the map then appending to result array
            result.append(str(digit_map[char]))
    if result:
        return ''.join(result) # converting to string with help of join
    return 'NONE'


for line in sys.stdin:
    response = process(line)
    print(response)
