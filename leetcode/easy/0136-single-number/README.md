# Single Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a  **non-empty**  array of integers `nums`, every element appears  *twice*  except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Original
Python3
 **Example 1:** 

 **Input:**  nums = [2,2,1]

 **Output:**  1

 **Example 2:** 

 **Input:**  nums = [4,1,2,1,2]

 **Output:**  4

 **Example 3:** 

 **Input:**  nums = [1]

 **Output:**  1

 

 **Constraints:** 

- 1 <= nums.length <= 3 * 104
- -3  *104 <= nums[i] <= 3*  104
- Each element in the array appears twice except for one element which appears only once.

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 64.72%)  
**Memory:** 21.3 MB (beats 43.57%)  
**Submitted:** 2026-11-23T15:34:16.991Z  

```py
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        x = 0

        for i in range(len(nums)):
            x = x ^ nums[i]

        return x
```

---

[View on LeetCode](https://leetcode.com/problems/single-number/)