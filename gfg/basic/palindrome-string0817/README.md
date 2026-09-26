# Palindrome String

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a string  **s**, find if it is a palindrome. A string is considered a palindrome if it reads the same forwards and backwards.

 **Examples :** 

```
Input: s = "abba"
Output: true
Explanation: "abba" reads the same forwards and backwards, so it is a palindrome.
```

```
Input: s = "abc" 
Output: false
Explanation: "abc" does not read the same forwards and backwards, so it is not a palindrome.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-26T18:05:47.633Z  

```py
class Solution:
    def isPalindrome(self, s):
        # code here
        def fun(s,high,low):
            l = high - low + 1
            if l == 0 or l == 1:
                return True
                
            if s[low] != s[high]:
                return False
                
            return fun(s,high - 1, low + 1)
            
        n = len(s)
        return fun(s, n - 1, 0)

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/palindrome-string0817/1)