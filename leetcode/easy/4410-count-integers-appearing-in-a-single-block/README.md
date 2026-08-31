# Q1. Count Integers Appearing in a Single Block

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer array `nums`.

An integer `x` is  **special**  if all occurrences of `x` in `nums` appear in a single  **contiguous**  block.

Return the number of  **distinct**  special integers in `nums`.

 

 **Example 1:** 

 **Input:**  nums = [1,2,2,1]

 **Output:**  1

 **Explanation:** 

- 1 appears at indices 0 and 3, forming two separate blocks, so it is not special.
- 2 appears in a single contiguous block at indices [1, 2], so it is special.

Therefore, there is one special integer.

 **Example 2:** 

 **Input:**  nums = [3,3,1,2,2,1]

 **Output:**  2

 **Explanation:** 

- 3 appears in a single contiguous block at indices [0, 1], so it is special.
- 1 appears at indices 2 and 5, forming two separate blocks, so it is not special.
- 2 appears in a single contiguous block at indices [3, 4], so it is special.

Therefore, there are two special integers.

 

 **Constraints:** 

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 66.67%)  
**Memory:** 19.3 MB (beats 100.00%)  
**Submitted:** 2026-08-31T18:05:58.426Z  

```py
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        f = {}
        l = {}
        freq = {}
        for i,x in enumerate(nums):
            if x not in f:
                f[x] = i
            l[x] = i
            freq[x] = freq.get(x,0) + 1
        c = 0

        for x in f:
            length = l[x] - f[x] + 1

            if length == freq[x]:
                c += 1
        return c
        
                
        
```

---

[View on LeetCode](https://leetcode.com/problems/count-integers-appearing-in-a-single-block/)