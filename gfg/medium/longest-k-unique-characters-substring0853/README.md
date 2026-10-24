# Longest Substring with K Uniques

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a string  **s**  consisting only lowercase alphabets and an integer  **k**. Your task is to find the  **length** of the  **longest substring**  that contains exactly  **k**  distinct characters.

 **Note :**  If no such substring exists, return  **-1**. 

 **Examples:** 

```
Input: s = "aabacbebebe", k = 3
Output: 7
Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.

```

```
Input: s = "aaaa", k = 2
Output: -1
Explanation: There's no substring with 2 distinct characters.

```

```
Input: s = "aabaaab", k = 2
Output: 7
Explanation: The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T12:37:11.784Z  

```py
class Solution:
    def longestKSubstr(self, s, k):
        # code here
        low = 0
        freq = {}
        max_len = -float('inf')
        for high in range(len(s)):
            freq[s[high]] = freq.get(s[high],0) + 1
            while len(freq) > k:
                freq[s[low]] -= 1
                if freq[s[low]] == 0:
                    del freq[s[low]]
                low += 1
                
            if len(freq) == k:
                l = high - low + 1
                max_len = max(max_len,l)
                    
        return -1 if max_len == -float('inf') else max_len                    
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1)