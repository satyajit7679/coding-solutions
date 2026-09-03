# Reverse Linked List II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return  *the reversed list*.

 

 **Example 1:** 

```
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

```

 **Example 2:** 

```
Input: head = [5], left = 1, right = 1
Output: [5]

```

 

 **Constraints:** 

- The number of nodes in the list is n.
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n

 

 **Follow up:**  Could you do it in one pass?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.4 MB (beats 25.84%)  
**Submitted:** 2026-09-03T18:33:41.093Z  

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None:
            return None

        if left == right:
            return head

        t = head
        before = None
        pos = 1

        # reach left position
        while pos < left:
            before = t
            t = t.next
            pos += 1

        curr = t
        prev = None

        times = right - left + 1

        # reverse
        while times:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            times -= 1

        # connect
        t.next = curr

        if before != None:
            before.next = prev
        else:
            head = prev

        return head
```

---

[View on LeetCode](https://leetcode.com/problems/reverse-linked-list-ii/)