# Rotate List

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the `head` of a linked list, rotate the list to the right by `k` places.

 

 **Example 1:** 

```
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

```

 **Example 2:** 

```
Input: head = [0,1,2], k = 4
Output: [2,0,1]

```

 

 **Constraints:** 

- The number of nodes in the list is in the range [0, 500].
- -100 <= Node.val <= 100
- 0 <= k <= 2 * 109

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 21.05%)  
**Memory:** 19.2 MB (beats 77.32%)  
**Submitted:** 2026-09-08T12:34:16.609Z  

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        n = 1
        last = head
        while last.next != None:
            n += 1
            last = last.next
        
        k = k % n
        if k == 0:
            return head
        
        last.next = head

        s = n - k
        t = head
        for _ in range(s - 1):
            t = t.next
        
        newhead = t.next
        t.next = None
        return newhead

```

---

[View on LeetCode](https://leetcode.com/problems/rotate-list/)