# Happy Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Write an algorithm to determine if a number `n` is happy.

A  **happy number**  is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return `true`  *if*  `n`  *is a happy number, and*  `false`  *if not*.

 

 **Example 1:** 

```
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

```

 **Example 2:** 

```
Input: n = 2
Output: false

```

 

 **Constraints:** 

- 1 <= n <= 231 - 1

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.2 MB (beats 62.18%)  
**Submitted:** 2026-08-22T18:30:42.843Z  

```py
class Solution:
    def cal_sum_squre(self, n):
        curr_sum = 0
        while n > 0:
            r = n % 10
            n = n // 10
            curr_sum += r * r
        return curr_sum
    def isHappy(self, n: int) -> bool:
        
        slow = n
        fast = n
        while True:
            slow = self.cal_sum_squre(slow)
            fast = self.cal_sum_squre(fast)
            fast = self.cal_sum_squre(fast)
            if fast == 1:
                return True
            if slow == fast:
                return False

        
```

---

[View on LeetCode](https://leetcode.com/problems/happy-number/)