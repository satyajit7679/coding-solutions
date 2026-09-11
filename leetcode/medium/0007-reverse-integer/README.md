# Reverse Integer

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a signed 32-bit integer `x`, return `x` *with its digits reversed*. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return `0`.

 **Assume the environment does not allow you to store 64-bit integers (signed or unsigned).** 

 

 **Example 1:** 

```
Input: x = 123
Output: 321

```

 **Example 2:** 

```
Input: x = -123
Output: -321

```

 **Example 3:** 

```
Input: x = 120
Output: 21

```

 

 **Constraints:** 

- -231 <= x <= 231 - 1

## Solution

**Language:** Python  
**Runtime:** 51 ms (beats 24.02%)  
**Memory:** 19.3 MB (beats 31.87%)  
**Submitted:** 2026-09-11T17:43:31.615Z  

```py
class Solution:
    def reverse(self, x: int) -> int:

        # Remember whether x is positive or negative
        sign = -1 if x < 0 else 1

        # Work with positive number
        x = abs(x)

        rev = 0

        while x > 0:

            # Get last digit
            digit = x % 10

            # Remove last digit
            x = x // 10

            # Check if adding this digit causes overflow
            if rev > (2**31 - 1 - digit) // 10:
                return 0

            # Add digit to reversed number
            rev = rev * 10 + digit

        # Put the original sign back
        return sign * rev
```

---

[View on LeetCode](https://leetcode.com/problems/reverse-integer/)