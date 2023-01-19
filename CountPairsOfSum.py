"""
Count pairs with given sum
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.

Example 1:

Input:
N = 4, K = 6
array[] = {1, 5, 7, 1}
Output: 2
Explanation:
array[0] + array[1] = 1 + 5 = 6
and array[1] + array[3] = 5 + 1 = 6.

Example 2:

Input:
N = 4, K = 2
array[] = {1, 1, 1, 1}
Output: 6
Explanation:
Each 1 will produce sum 2 with any 1.

Your Task:
You don't need to read input or print anything. Your task is to complete the function getPairsCount() which takes array[], n and k as input parameters and returns the number of pairs that have sum K.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 105
1 <= K <= 108
1 <= Arr[i] <= 106

"""


# Time complexity O(n * n) , Space O(1)
def bruteForce(arr, target):
    count = 0
    for x in range(0, len(arr)):
        for y in range(x + 1, len(arr)):
            if arr[x] + arr[y] == target:
                count += 1
    print(" Number of pair counts are  : ", count)
    return count


array = [1, 5, 7, 1]
target = 6
bruteForce(array, target)



def optimalUsingMap(arr , target):
    map = [0] * 1000
    count = 0
    for x in range(0, len(arr)):
        map[arr[x]] +=1
    # Iterate through all the elements and increment the count (every pair is counted twice)
    for x in range(0, len(arr)):
        count += map[target - arr[x]]
        # if (array[x], array[x]) , satisfy then we need to decrease the count by 1
        if target - arr[x] == arr[x]:
            count -= 1
    return int(count/2)


arr = [1, 1, 1, 1]
sum = 2

print(" Count of pairs is", optimalUsingMap(arr, sum))


