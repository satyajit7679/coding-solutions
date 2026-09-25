# Replace Consecutive Two Same with One

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string  **s**, consisting of lowercase alphabets. Remove consecutive duplicate characters from the string. 

 **Example:** 

```
Input: s = "aabb"
Output: "ab" 
Explanation: The character 'a' at index 2 is the same as 'a' at index 1, so it is removed.Similarly, the character 'b' at index 4 is the same as 'b' at index 3, so it is removed. The final string is "ab".

```

```
Input: s = "aabaa"
Output: "aba"
Explanation: The character 'a' at index 2 is the same as 'a' at index 1, so it is removed. The character 'a' at index 5 is the same as 'a' at index 4, so it is removed. The final string is "aba".
```

```
Input: s = "aaaa"
Output: "a"
Explanation: "aaaa" => "aaa" => "aa" => "a" 
```

 **Constraints:** 
1 ≤ n ≤ 106
All characters in the string are lowercase English alphabets.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-25T11:11:18.210Z  

```py
class Solution:
    def removeDuplicates(self, s):
        # code here
        i = 1
        res = s[0]
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                res = res + s[i]
        return res
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/consecutive-elements2306/1)