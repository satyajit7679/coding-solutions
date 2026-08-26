class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        res = ""
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
                continue

            if stack[-1] == s[i]:
                stack.pop()
                continue
            else:
                stack.append(s[i])
        
        while stack:
            res = stack.pop() + res
        
        return res

        