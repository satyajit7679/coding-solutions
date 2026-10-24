# Find All Anagrams in a String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in  **any order**.

 

 **Example 1:** 

```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

```

 **Example 2:** 

```
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

```

 

 **Constraints:** 

- 1 <= s.length, p.length <= 3 * 104
- s and p consist of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 41 ms (beats 53.27%)  
**Memory:** 19.7 MB (beats 66.78%)  
**Submitted:** 2026-10-24T17:36:09.467Z  

```py
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        res = []
        f = {}
        w = {}
        low = 0
        for ch in p:
            f[ch] = f.get(ch,0) + 1

        for high in range(len(s)):
            w[s[high]] = w.get(s[high],0) + 1

            if high - low + 1 > len(p):
                w[s[low]] -= 1

                if w[s[low]] == 0:
                    del w[s[low]]

                low += 1

            if w == f:
                res.append(low)

        return res

        
```

---

[View on LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/)