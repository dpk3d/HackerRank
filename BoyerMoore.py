"""
https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/


Pattern searching is an important problem in computer science. When we do search for a string in a notepad/word file,
browser, or database, pattern searching algorithms are used to show the search results. A typical problem statement would be-
Given a text txt[0..n-1] and a pattern pat[0..m-1] where n is the length of the text and m is the length of the pattern,
write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.

Examples:

Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12

"""

# Python3 Program for Bad Character Heuristic of Boyer Moore String Matching Algorithm

NO_OF_CHARS = 256


def badCharHeuristic(string, size):
    '''
	The preprocessing function for
	Boyer Moore's bad character heuristic
	'''

    # Initialize all occurrence as -1
    badChar = [-1] * NO_OF_CHARS

    # Fill the actual value of last occurrence
    for i in range(size):
        badChar[ord(string[i])] = i;

    # return initialized list
    return badChar


def search(txt, pat):
    '''
	A pattern searching function that uses Bad Character
	Heuristic of Boyer Moore Algorithm
	'''

    m = len(pat)
    n = len(txt)

    # create the bad character list by calling
    # the preprocessing function badCharHeuristic()
    # for given pattern
    badChar = badCharHeuristic(pat, m)

    # s is shift of the pattern with respect to text
    s = 0
    while (s <= n - m):
        j = m - 1

        # Keep reducing index j of pattern while
        # characters of pattern and text are matching
        # at this shift s
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1

        # If the pattern is present at current shift,
        # then index j will become -1 after the above loop
        if j < 0:
            print("Pattern occur at shift = {}".format(s))

            ''' Shift the pattern so that the next character in text aligns with the last occurrence of it in pattern.
				The condition s+m < n is necessary for the case when pattern occurs at the end of text
			'''
            s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
        else:
            '''
			Shift the pattern so that the bad character in text aligns with the last occurrence of it in pattern.
			 The max function is used to make sure that we get a positive shift.
			  We may get a negative shift if the last occurrence of bad character in pattern is on the right side of the current character.
			'''
            s += max(1, j - badChar[ord(txt[s + j])])


# Driver program to test above function
def main():
    txt = "ABAAABCD"
    pat = "ABC"
    search(txt, pat)


if __name__ == '__main__':
    main()

# This code is contributed by Atul Kumar
# (www.facebook.com/atul.kr.007)
