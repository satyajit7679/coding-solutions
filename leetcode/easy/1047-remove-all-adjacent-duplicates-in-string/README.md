# Remove All Adjacent Duplicates In String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a string `s` consisting of lowercase English letters. A  **duplicate removal**  consists of choosing two  **adjacent**  and  **equal**  letters and removing them.

We repeatedly make  **duplicate removals**  on `s` until we no longer can.

Return  *the final string after all such duplicate removals have been made*. It can be proven that the answer is  **unique**.

 

 **Example 1:** 

```
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

```

 **Example 2:** 

```
Input: s = "azxxzy"
Output: "ay"

```

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 12 ms (beats 98.66%)  
**Memory:** 20 MB (beats 90.93%)  
**Submitted:** 2026-08-26T14:38:37.476Z  

```py
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

        
```

---

[View on LeetCode](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)