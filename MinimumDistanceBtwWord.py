# Asked in Visa Interview
# tom and jerry are good friend tom likes to chase jerry but jerry does think it is a good idea that tom chase  plays
# minimum distance between k1, k2
# k1 = tom
# k2 = jerry
# d = 1

def minDistanceBruteForce(sentence, k1, k2):
    if k1 == k2:
        return 0

    splited = sentence.split(" ")
    splittedLen = len(splited)

    # tempIndex = 0
    # result = 0
    for word in range(len(splited)):
        if splited[word] == k1:
            for seek in range(len(splited)):
                if splited[seek] == k2:
                    currentIndex = word - seek
                    if currentIndex < splittedLen:
                        splittedLen = currentIndex
    return splittedLen
