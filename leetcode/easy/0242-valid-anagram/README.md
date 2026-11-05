# Valid Anagram

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

 

 **Example 1:** 

 **Input:**  s = "anagram", t = "nagaram"

 **Output:**  true

 **Example 2:** 

 **Input:**  s = "rat", t = "car"

 **Output:**  false

 

 **Constraints:** 

- 1 <= s.length, t.length <= 5 * 104
- s and t consist of lowercase English letters.

 

 **Follow up:**  What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Solution

**Language:** Python  
**Runtime:** 13 ms (beats 50.72%)  
**Memory:** 19.4 MB (beats 46.40%)  
**Submitted:** 2026-11-05T14:48:32.848Z  

```py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        f = {}
        w = {}
        for ch in s:
            if ch in f:
                f[ch] += 1
            else:
                f[ch] = 1
        
        for ch in t:
            if ch not in f:
                return False
            
            f[ch] -= 1

            if f[ch] < 0:
                return False

        return True
```

---

[View on LeetCode](https://leetcode.com/problems/valid-anagram/)