# Longest Substring Without Repeating Characters

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s`, find the length of the  **longest**   **substring**  without duplicate characters.

 

 **Example 1:** 

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

```

 **Example 2:** 

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

```

 **Example 3:** 

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

 

 **Constraints:** 

- 0 <= s.length <= 105
- s consists of English letters, digits, symbols and spaces.

## Solution

**Language:** Python  
**Runtime:** 368 ms (beats 13.92%)  
**Memory:** 19.9 MB (beats 74.02%)  
**Submitted:** 2026-10-24T17:01:34.762Z  

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = 0
        low = 0
        max_len = 0
        l = 0
        freq = {}
        for high in range(len(s)):
            freq[s[high]] = freq.get(s[high],0) + 1
            k = high - low + 1
            while len(freq) < k:
                freq[s[low]] -= 1
                if freq[s[low]] == 0:
                    del freq[s[low]]
                low += 1
                k = high - low + 1

            l = high - low + 1
            max_len = max(max_len,l)

        return max_len 
        
```

---

[View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)