# Problem Statement. 
"""
Charlemagne, the King of Frankia, is considering building some castles on the border with Servia. 
The border is divided into N segments. The King knows the height of the terrain in each segment of the border.
The height of each segment of terrain is stored in array A, with A[P] denoting the height of the P-th segment of the border. 
The King has decided to build a castle on top of every hill and in the bottom of every valley.
Let [P ..Q] denotes group of consecutive segments from P to Q inclusive such that ( 0 <= P <= Q <= N - 1).
Segments [P..Q] from a hill or valley if all the following conditions are satisfied.
 The Terrain Height of each segment  from P to Q is the same (A[P] = A[P + 1] = ... = A[Q])
 If P > 0 then A[P - 1] < A[P] For a Hill or A[P - 1] > A[P]  For a Valley .
 If Q < N - 1  then  A[Q + 1] < A[Q] for a Hill or A[Q + 1] > A[Q] for a Valley.
 That is a Hill is higher than it's surrounding and valley is lower than it's surroundings.
 
 For Example consider the following  array A = [2,2,3,4,3,3,2,2,1,1,2,5]
 There are two hills: [3..3] and [11..11] . There are two valleys : [0..1] and [ 8..9].
 Write Function :
 """

#Ideation of Hill     -- A < B < C
#Ideation of Valley   -- A > B <= C < D
 
def solution(arr):
    # Declaring Variables
    final_arr = []
    valley = 0
    hill = 0 
    for index, item in enumerate(arr):
        if index > 0 and (index+1) < len(arr):
            if arr[index-1] < arr[index] < arr[index+1]:
            #print ("hill", index+1, arr[index-1], arr[index], arr[index+1])
                final_arr.append(['hill', index+1])
                hill+=1
            #final_arr([index+1, [arr[index-1], arr[index], arr[index+1]]])
            if (arr[index-1] > arr[index]) and (arr[index+1] < arr[index+2]):
            #print ("valley",index+1, arr[index-1], arr[index], arr[index+1])
                final_arr.append(['valley', index+1])
                valley+=1
        if index == 0 and index +2 < len(arr):
            if (arr[index+1] < arr[index+2]):
            #print ("valley",index+1, arr[index-1])
                final_arr.append(['valley', index+1])
                valley+=1
    if hill == valley and hill == 0 and len(arr) > 0:
        return 1
    return hill + valley
