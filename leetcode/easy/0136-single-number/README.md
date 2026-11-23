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
**Runtime:** 10 ms (beats 16.10%)  
**Memory:** 21.5 MB (beats 15.65%)  
**Submitted:** 2026-11-23T15:33:55.440Z  

```py
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        for i in freq:
            if freq[i] == 1:
                return i
        
```

---

[View on LeetCode](https://leetcode.com/problems/single-number/)