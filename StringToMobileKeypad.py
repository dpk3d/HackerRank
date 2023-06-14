"""
https://www.geeksforgeeks.org/convert-sentence-equivalent-mobile-numeric-keypad-sequence/

Given a sentence in the form of a string, convert it into its equivalent mobile numeric keypad sequence.

Input: GEEKSFORGEEKS
Output: 4333355777733366677743333557777

"""


def printNumericSequence(given_string, keypad_arr):

    str_len = len(given_string)
    result = ""
    for x in range(str_len):
        if given_string[x] == ' ':
            result = result + "0"
        else:
            # calculate index for each character
            index = ord(given_string[x]) - ord('A')
            result = result + keypad_arr[index]
    return result


input_string = "GEEKSFORGEEKS"
keypad_arr = ["2", "22", "222",
           "3", "33", "333",
           "4", "44", "444",
           "5", "55", "555",
           "6", "66", "666",
           "7", "77", "777", "7777",
           "8", "88", "888",
           "9", "99", "999", "9999"]

print("The Numeric Sequence for given string is : ",printNumericSequence(input_string,keypad_arr))
# The Numeric Sequence for given string is :  4333355777733366677743333557777

print("The Numeric Sequence for given string is : ",printNumericSequence("DEEPAKSINGH",keypad_arr))
# The Numeric Sequence for given string is :  333337255777744466444


