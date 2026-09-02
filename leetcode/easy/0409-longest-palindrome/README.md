# Longest Palindrome

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s` which consists of lowercase or uppercase letters, return the length of the  **longest palindrome**  that can be built with those letters.

Letters are  **case sensitive**, for example, `"Aa"` is not considered a palindrome.

 

 **Example 1:** 

```
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

```

 **Example 2:** 

```
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

```

 

 **Constraints:** 

- 1 <= s.length <= 2000
- s consists of lowercase and/or uppercase English letters only.

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 53.93%)  
**Memory:** 19.2 MB (beats 67.20%)  
**Submitted:** 2026-09-02T16:02:23.348Z  

```py
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        res = 0
        odd = False
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        for ch in freq:
            val = freq[ch]
            if val % 2 == 0:
                res += val
            else:
                res += val - 1
                odd = True
        
        if odd:
            res += 1
        
        return res
        

        
```

---

[View on LeetCode](https://leetcode.com/problems/longest-palindrome/)