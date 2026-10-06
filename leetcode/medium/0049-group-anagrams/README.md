# Group Anagrams

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of strings `strs`, group the anagrams together. You can return the answer in  **any order**.

 

 **Example 1:** 

 **Input:**  strs = ["eat","tea","tan","ate","nat","bat"]

 **Output:**  [["bat"],["nat","tan"],["ate","eat","tea"]]

 **Explanation:** 

- There is no string in strs that can be rearranged to form "bat".
- The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
- The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

 **Example 2:** 

 **Input:**  strs = [""]

 **Output:**  [[""]]

 **Example 3:** 

 **Input:**  strs = ["a"]

 **Output:**  [["a"]]

 

 **Constraints:** 

- 1 <= strs.length <= 104
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 15 ms (beats 42.19%)  
**Memory:** 21.9 MB (beats 79.52%)  
**Submitted:** 2026-10-06T15:30:01.633Z  

```py
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group={}
        for s in strs:
            key="".join(sorted(s))
            if key not in group:
                group[key]=[]
            group[key].append(s)
        return list(group.values())        


        
```

---

[View on LeetCode](https://leetcode.com/problems/group-anagrams/)