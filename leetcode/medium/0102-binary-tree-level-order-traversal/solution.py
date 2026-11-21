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
                