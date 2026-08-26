# class Solution:
#     def removeDuplicates(self, s: str) -> str:
#         stack = []
#         res = ""
#         for i in range(len(s)):
#             if not stack:
#                 stack.append(s[i])
#                 continue

#             if stack[-1] == s[i]:
#                 stack.pop()
#                 continue
#             else:
#                 stack.append(s[i])
        
#         while stack:
#             res = stack.pop() + res
        
#         return res


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)

        