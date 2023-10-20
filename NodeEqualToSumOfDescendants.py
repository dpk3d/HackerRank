"""

Given the root of a binary tree, return the number of nodes where the value of the node is equal
 to  the sum of the values of its descendants.
 A descendant of a node 'x' is any node that is on the path from node 'x' to some leaf node.


Input:

          10
         /  \
        3    4
       / \
      2   1


Output: 2

[10 and 3 are the nodes]

"""

from dataclasses import dataclass
from typing import Optional

from treenode import TreeNode


@dataclass(frozen=True)
class T:
    totalSum: int
    totalCount: int


# Time: O(n)
# Space: O(h)
class Solution:
    def countOfNodeEqualToDescendants(self, root: Optional[TreeNode]) -> int:
        def treeDFS(root: Optional[TreeNode]) -> T:
            if not root:
                return T(0, 0)
            leftTree = treeDFS(root.left)
            rightTree = treeDFS(root.right)
            return T(root.val + leftTree.totalSum + rightTree.totalSum,
                     leftTree.totalCount + rightTree.totalCount +
                     (1 if root.val == leftTree.totalSum + rightTree.totalSum else 0))

        return treeDFS(root).totalCount
