# Ransom Note

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings `ransomNote` and `magazine`, return `true` *if* `ransomNote` *can be constructed by using the letters from* `magazine` *and* `false` *otherwise*.

Each letter in `magazine` can only be used once in `ransomNote`.

 

 **Example 1:** 

```
Input: ransomNote = "a", magazine = "b"
Output: false

```

 **Example 2:** 

```
Input: ransomNote = "aa", magazine = "ab"
Output: false

```

 **Example 3:** 

```
Input: ransomNote = "aa", magazine = "aab"
Output: true

```

 

 **Constraints:** 

- 1 <= ransomNote.length, magazine.length <= 105
- ransomNote and magazine consist of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 32 ms (beats 7.16%)  
**Memory:** 19.5 MB (beats 72.82%)  
**Submitted:** 2026-08-31T19:37:52.072Z  

```py
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        have = {}
        need = {}

        for i in range(len(ransomNote)):
            need[ransomNote[i]] = need.get(ransomNote[i], 0) + 1

        for i in range(len(magazine)):
            have[magazine[i]] = have.get(magazine[i], 0) + 1

        for key, value in need.items():
            if key not in have or value > have[key]:
                return False

        return True
```

---

[View on LeetCode](https://leetcode.com/problems/ransom-note/)