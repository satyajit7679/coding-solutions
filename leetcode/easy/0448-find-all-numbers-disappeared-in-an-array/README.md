# Find All Numbers Disappeared in an Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return  *an array of all the integers in the range*  `[1, n]`  *that do not appear in*  `nums`.

 

 **Example 1:** 

```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

```

 **Example 2:** 

```
Input: nums = [1,1]
Output: [2]

```

 

 **Constraints:** 

- n == nums.length
- 1 <= n <= 105
- 1 <= nums[i] <= n

 

 **Follow up:**  Could you do it without extra space and in `O(n)` runtime? You may assume the returned list does not count as extra space.

## Solution

**Language:** Python  
**Runtime:** 57 ms (beats 7.76%)  
**Memory:** 40.8 MB (beats 5.13%)  
**Submitted:** 2026-08-22T15:16:23.117Z  

```py
class Solution:
    def findDisappearedNumbers(self, arr: List[int]) -> List[int]:
        freq = {}
        res = []
        n = len(arr)
        for i in range(1,n + 1):
            freq[i] = 0
        for i in range(n):
            freq[arr[i]] = 1
        for i in range(1,n + 1):
            if freq[i] == 0:
                res.append(i)
        return res
```

---

[View on LeetCode](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)