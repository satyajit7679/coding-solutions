# Reverse Nodes in k-Group

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return  *the modified list*.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

 **Example 1:** 

```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

```

 **Example 2:** 

```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

```

 

 **Constraints:** 

- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

 

 **Follow-up:**  Can you solve the problem in `O(1)` extra memory space?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 20.4 MB (beats 47.22%)  
**Submitted:** 2026-09-07T18:51:04.403Z  

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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        left = head
        res = None
        prevleft = None

        while left:

            # Find the second node of the pair
            right = left

            for i in range((k - 1)):
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
            newhead, nextnode = self.reverse(left, k)

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

[View on LeetCode](https://leetcode.com/problems/reverse-nodes-in-k-group/)