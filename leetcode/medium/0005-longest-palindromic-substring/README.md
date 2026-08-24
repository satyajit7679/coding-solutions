# Longest Palindromic Substring

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s`, return  *the longest*   *palindromic*   *substring*  in `s`.

 

 **Example 1:** 

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

```

 **Example 2:** 

```
Input: s = "cbbd"
Output: "bb"

```

 

 **Constraints:** 

- 1 <= s.length <= 1000
- s consist of only digits and English letters.

## Solution

**Language:** Python  
**Runtime:** 231 ms (beats 85.10%)  
**Memory:** 19.3 MB (beats 69.35%)  
**Submitted:** 2026-08-24T18:36:54.701Z  

```py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            ans1 = self.expend(s, i, i)
            ans2 = self.expend(s, i, i+1)
            if len(ans1) > len(res):
                res = ans1

            if len(ans2) > len(res):
                res = ans2
        return res

    def expend(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right] 
        
```

---

[View on LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)