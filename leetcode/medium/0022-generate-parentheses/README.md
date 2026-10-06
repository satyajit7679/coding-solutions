# Generate Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given `n` pairs of parentheses, write a function to  *generate all combinations of well-formed parentheses*.

 

 **Example 1:** 

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

```

 **Example 2:** 

```
Input: n = 1
Output: ["()"]

```

 

 **Constraints:** 

- 1 <= n <= 8

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 42.23%)  
**Memory:** 19.3 MB (beats 95.55%)  
**Submitted:** 2026-10-06T15:12:00.595Z  

```py
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        def fun(open, close, n, temp, res):

            if open == n and close == n:
                res.append(temp)
                return

            if open < n:
                temp = temp + '('
                fun(open + 1, close, n, temp, res)
                temp = temp[:-1]

            if close < open:
                temp = temp + ')'
                fun(open, close + 1, n, temp, res)
                temp = temp[:-1]

        res = []
        fun(0, 0, n, "", res)

        return res
```

---

[View on LeetCode](https://leetcode.com/problems/generate-parentheses/)