# Valid Palindrome

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

A phrase is a  **palindrome**  if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` *if it is a  **palindrome**, or* `false` *otherwise*.

 

Original
Python3
 **Example 1:** 

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

```

 **Example 2:** 

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

```

 **Example 3:** 

```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

```

 

 **Constraints:** 

- 1 <= s.length <= 2 * 105
- s consists only of printable ASCII characters.

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 82.04%)  
**Memory:** 19.4 MB (beats 97.40%)  
**Submitted:** 2026-11-15T05:43:20.376Z  

```py
class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        for ch in s:
            if ch.isalnum():
                r += ch.lower()
        
        i = 0
        j = len(r) - 1
        while i < j:
            if r[i] != r[j]:
                return False
            i += 1
            j -= 1

        return True
            
```

---

[View on LeetCode](https://leetcode.com/problems/valid-palindrome/)