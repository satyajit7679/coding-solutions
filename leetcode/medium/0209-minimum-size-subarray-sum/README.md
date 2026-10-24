# Minimum Size Subarray Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of positive integers `nums` and a positive integer `target`, return  *the  **minimal length**  of a  **subarray**  whose sum is greater than or equal to*  `target`. If there is no such subarray, return `0` instead.

 

 **Example 1:** 

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

```

 **Example 2:** 

```
Input: target = 4, nums = [1,4,4]
Output: 1

```

 **Example 3:** 

```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

```

 

 **Constraints:** 

- 1 <= target <= 109
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 104

 

 **Follow up:**  If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.

## Solution

**Language:** Python  
**Runtime:** 15 ms (beats 88.63%)  
**Memory:** 30.5 MB (beats 46.46%)  
**Submitted:** 2026-10-24T17:15:33.489Z  

```py
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        low = 0
        t = 0
        min_len = float('inf')
        for high in range(len(nums)):
            t += nums[high]
            while t >= target:
                l = high - low + 1
                min_len = min(l,min_len)
                t -= nums[low]
                low += 1
        return 0 if min_len == float('inf') else min_len

        
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/)