# Binary Tree Level Order Traversal

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the `root` of a binary tree, return  *the level order traversal of its nodes' values*. (i.e., from left to right, level by level).

 

 **Example 1:** 

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

```

 **Example 2:** 

```
Input: root = [1]
Output: [[1]]

```

 **Example 3:** 

```
Input: root = []
Output: []

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.9 MB (beats 41.45%)  
**Submitted:** 2026-11-21T06:47:29.557Z  

```py
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res = []
        if root == None:
            return res

        q = deque()
        q.append(root)

        while len(q) > 0:
            lvlsize = len(q)
            temp = []
            while lvlsize > 0:
                t = q.popleft()
                temp.append(t.val)
                if t.left != None:
                    q.append(t.left)

                if t.right != None:
                    q.append(t.right)

                lvlsize -= 1
                
            res.append(temp)
        return res
                
```

---

[View on LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/)