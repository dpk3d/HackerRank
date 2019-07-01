# Hacker Rank Prioroties Input is [ 1, 3, 7, 3] and Ouput should be [1, 2, 3, 2] 
# Another Input is [2,9,3,3,3] and Ouptput is [1, 3,2, 1, 2]
#


def priorities(inputArr):
    temp = sorted(set(inputArr))
    ans = []
    for each in inputArr:
        ans.append((temp.index(each)+1))
    print (ans)


if _name_ == '_main_':
    coins = [2,9,3,2,3]
    print (inputArr)
    priorities(inputArr)
    
