# Maximum Number of Balloons

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `text`, you want to use the characters of `text` to form as many instances of the word  **"balloon"**  as possible.

You can use each character in `text`  **at most once**. Return the maximum number of instances that can be formed.

 

 **Example 1:** 

```
Input: text = "nlaebolko"
Output: 1

```

 **Example 2:** 

```
Input: text = "loonbalxballpoon"
Output: 2

```

 **Example 3:** 

```
Input: text = "leetcode"
Output: 0

```

 

 **Constraints:** 

- 1 <= text.length <= 104
- text consists of lower case English letters only.

 

 **Note:**  This question is the same as 2287: Rearrange Characters to Make Target String.

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 62.56%)  
**Memory:** 19.3 MB (beats 40.33%)  
**Submitted:** 2026-09-02T15:33:53.880Z  

```py
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = "balloon"
        need = {}
        have = {}
        res = float('inf')
        for ch in s:
            need[ch] = need.get(ch,0) + 1
        for ch in text:
            have[ch] = have.get(ch,0) + 1
        for ch in need:
            times = have.get(ch, 0) // need[ch]
            res = min(res,times)  
        return res
        
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-number-of-balloons/)