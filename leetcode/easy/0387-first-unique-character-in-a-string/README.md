# First Unique Character in a String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s`, find the  **first**  non-repeating character in it and return its index. If it  **does not**  exist, return `-1`.

 

 **Example 1:** 

 **Input:**  s = "leetcode"

 **Output:**  0

 **Explanation:** 

The character `'l'` at index 0 is the first character that does not occur at any other index.

 **Example 2:** 

 **Input:**  s = "loveleetcode"

 **Output:**  2

 **Example 3:** 

 **Input:**  s = "aabb"

 **Output:**  -1

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of only lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 65 ms (beats 69.99%)  
**Memory:** 19.7 MB (beats 59.41%)  
**Submitted:** 2026-08-31T19:08:03.998Z  

```py
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1
        
```

---

[View on LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/)