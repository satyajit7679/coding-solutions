# Same Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

 **Example 1:** 

```
Input: p = [1,2,3], q = [1,2,3]
Output: true

```

 **Example 2:** 

```
Input: p = [1,2], q = [1,null,2]
Output: false

```

 **Example 3:** 

```
Input: p = [1,2,1], q = [1,1,2]
Output: false

```

 

 **Constraints:** 

- The number of nodes in both trees is in the range [0, 100].
- -104 <= Node.val <= 104

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 4.76%)  
**Memory:** 19.1 MB (beats 78.20%)  
**Submitted:** 2026-11-23T12:01:48.693Z  

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:

        def fun(p, q):
            if p == None and q == None:
                return True

            if p == None or q == None:
                return False

            if p.val != q.val:
                return False

            r1 = fun(p.left, q.left)
            r2 = fun(p.right, q.right)

            return r1 and r2

        return fun(p, q)

```

---

[View on LeetCode](https://leetcode.com/problems/same-tree/)