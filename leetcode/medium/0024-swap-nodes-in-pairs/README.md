# Swap Nodes in Pairs

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

 **Example 1:** 

 **Input:**  head = [1,2,3,4]

 **Output:**  [2,1,4,3]

 **Explanation:** 

 **Example 2:** 

 **Input:**  head = []

 **Output:**  []

 **Example 3:** 

 **Input:**  head = [1]

 **Output:**  [1]

 **Example 4:** 

 **Input:**  head = [1,2,3]

 **Output:**  [2,1,3]

 

 **Constraints:** 

- The number of nodes in the list is in the range [0, 100].
- 0 <= Node.val <= 100

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.4 MB (beats 22.56%)  
**Submitted:** 2026-09-07T17:39:53.266Z  

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self, head, times):
        prev = None
        curr = head

        while times > 0:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            times -= 1

        return prev, curr

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        left = head
        res = None
        prevleft = None

        while left:

            # Find the second node of the pair
            right = left

            for i in range(1):
                if right is None:
                    break
                right = right.next

            # Only one node remains
            if right is None:
                if prevleft:
                    prevleft.next = left
                break

            # Save node after the pair
            nextleft = right.next

            # Reverse the pair
            newhead, nextnode = self.reverse(left, 2)

            # Connect previous part to reversed pair
            if prevleft:
                prevleft.next = newhead
            else:
                res = newhead

            # left is now the second node of the reversed pair
            prevleft = left

            # Move to next pair
            left = nextleft

        return res
```

---

[View on LeetCode](https://leetcode.com/problems/swap-nodes-in-pairs/)