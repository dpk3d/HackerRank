"""

Given a binary tree, count the number of binary search trees present in it.

https://www.geeksforgeeks.org/count-the-number-of-binary-search-trees-present-in-a-binary-tree/

"""


# Time Complexity : O(n)
# Space Complexity : O(tree height)

numBST = 0
def traverse(root):
    global numBST
    leftComplies = True
    rightComplies = True
    rootRange = [root.val, root.val]
    if root.left != None:
        leftResult = traverse(root.left)
        leftComplies = leftResult[0] and leftResult[1][1] < root.val
        rootRange[0] = leftResult[1][0]
    if root.right != None:
        rightResult = traverse(root.right)
        rightComplies = rightResult[0] and rightResult[1][0] > root.val
        rootRange[1] = rightResult[1][1]
    if leftComplies and rightComplies:
        numBST += 1
    return (leftComplies and rightComplies, rootRange)





# Python program to count number of Binary search
# trees in a given Binary Tree
INT_MIN = -2 ** 31
INT_MAX = 2 ** 31


class newNode():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Returns information about subtree such as number of BST's it has

# Time Complexity : O(n)
# Space Complexity : O(tree height)
# This code is copied from Geeksforgeekss not mine solution
def NumberOfBST(root):
    # Base case
    if (root == None):
        return 0, INT_MIN, INT_MAX, True

    # If leaf node then return from function and store information about the leaf node
    if (root.left == None and root.right == None):
        return 1, root.data, root.data, True

    # Store information about the left subtree
    L = NumberOfBST(root.left)

    # Store information about the right subtree
    R = NumberOfBST(root.right)

    # Create a node that has to be returned
    bst = [0] * 4
    bst[2] = min(root.data, (min(L[2], R[2])))
    bst[1] = max(root.data, (max(L[1], R[1])))

    # If whole tree rooted under the  current root is BST
    if (L[3] and R[3] and root.data > L[1] and root.data < R[2]):

        # Update the number of BSTs
        bst[3] = True
        bst[0] = 1 + L[0] + R[0]

    # If the whole tree is not a BST, update the number of BSTs
    else:
        bst[3] = False
        bst[0] = L[0] + R[0]

    return bst


# Driver code
if __name__ == '__main__':
    root = newNode(5)
    root.left = newNode(9)
    root.right = newNode(3)
    root.left.left = newNode(6)
    root.right.right = newNode(4)
    root.left.left.left = newNode(8)
    root.left.left.right = newNode(7)

    print(NumberOfBST(root)[0])