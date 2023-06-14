"""

https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/

Given a text txt[0. . .n-1] and a pattern pat[0. . .m-1],
 write a function search(char pat[], char txt[])
 that prints all occurrences of pat[] in txt[]. You may assume that n > m.

Examples:

    Input:  txt[] = “THIS IS A TEST TEXT”, pat[] = “TEST”
    Output: Pattern found at index 10

    Input:  txt[] =  “AABAACAADAABAABA”, pat[] =  “AABA”
    Output: Pattern found at index 0
                  Pattern found at index 9
                  Pattern found at index 12

"""


# Time Complexity : O(nm)
# Space Complexity : O(n)
# This approach will only print the starting index of the string, not all.
def pattern_matching(haystack, needle):
    if needle == haystack:
        return 0
    x = 0
    y = len(needle)
    while y <= len(haystack):
        currentNeedle = haystack[x:y]
        if currentNeedle == needle:
            return x
        x += 1
        y += 1
    return -1


inputStr = "THIS IS A TEST TEXT"
pattern = "TEST"
print("Result of Pattern Matching Index is : ", pattern_matching(inputStr, pattern))


# Result of Pattern Matching Index is :  10


# Rabin Karp slides the pattern one by one and also matches the hash value of a current substring text
# If values matches then only it starts matches the individual characters
# Hash Function here calculates an integer value , i.e. numeric value of a string.
def rabin_karp_pattern_search(inputStr, pattern, primeNumber):
    input_string_len = len(inputStr)
    pattern_len = len(pattern)
    x = y = 0
    hash_value_pattern = 0
    hash_value_input_str = 0
    hash_value = 1
    character = 256
    for x in range(pattern_len - 1):
        hash_value = (hash_value * character) % primeNumber
    for x in range(pattern_len):
        hash_value_pattern = (character * hash_value_pattern + ord(pattern[x])) % primeNumber
        hash_value_input_str = (character * hash_value_input_str + ord(inputStr[x])) % primeNumber
    for x in range(input_string_len - pattern_len + 1):
        if hash_value_pattern == hash_value_input_str:
            for y in range(pattern_len):
                if inputStr[x + y] != pattern[y]:
                    break
                else:
                    y += 1
            if y == pattern_len:
                print("Pattern found at index " + str(x))
                # Pattern found at index 0
                # Pattern found at index 10
        if x < input_string_len - pattern_len:
            hash_value_input_str = (character * (hash_value_input_str - ord(inputStr[x]) * hash_value) + ord(
                inputStr[x + pattern_len])) % primeNumber
            if hash_value_input_str < 0:
                hash_value_input_str = hash_value_input_str + primeNumber


input_str = "GEEKS FOR GEEKS"
pat = "GEEK"
prime = 101
rabin_karp_pattern_search(input_str, pat, prime)
