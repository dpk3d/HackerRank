"""

https://leetcode.com/problems/intersection-of-two-linked-lists/description/


"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Using Hashset
# Time Complexity : O( m + n)
# Space Complexity : O(n)
# Store elements of headA in a hashset and iterate through headB and if match found return.


def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    first_set = set()
    curr = headA

    while curr:
        first_set.add(curr)
        curr = curr.next

    curr = headB
    while curr:
        if curr in first_set:
            return curr
        curr = curr.next

    return None


# Optimal Solution : Two Pointer Approach
# Time Complexity :  O(m + n)
# Space Complexity : O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    one = headA
    two = headB
    while one != two: # checking the hash object
        one = headB if one is None else one.next
        two = headA if two is None else two.next
    return one
