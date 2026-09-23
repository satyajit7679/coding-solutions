# Rotate Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

 

 **Example 1:** 

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

```

 **Example 2:** 

```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -231 <= nums[i] <= 231 - 1
- 0 <= k <= 105

 

 **Follow up:** 

- Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
- Could you do it in-place with O(1) extra space?

## Solution

**Language:** Python  
**Runtime:** 125 ms (beats 33.31%)  
**Memory:** 35.1 MB (beats 38.46%)  
**Submitted:** 2026-09-23T15:03:48.823Z  

```py
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseNums(nums,low,high):
            while low < high:
                nums[low],nums[high] = nums[high],nums[low]
                low += 1
                high -= 1
            return nums

        n = len(nums)
        k = k % n

        reverseNums(nums,0,n - 1)
        reverseNums(nums,0,k - 1)
        reverseNums(nums,k,n - 1)
        
        
```

---

[View on LeetCode](https://leetcode.com/problems/rotate-array/)