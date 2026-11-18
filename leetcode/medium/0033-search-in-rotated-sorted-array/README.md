# Search in Rotated Sorted Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

There is an integer array `nums` sorted in ascending order (with  **distinct**  values).

Prior to being passed to your function, `nums` is  **possibly left rotated**  at an unknown index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1],..., nums[n-1], nums[0], nums[1],..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be left rotated by `3` indices and become `[4,5,6,7,0,1,2]`.

Given the array `nums`  **after**  the possible rotation and an integer `target`, return  *the index of* `target` *if it is in* `nums` *, or* `-1` *if it is not in* `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

 

Original
Python3
 **Example 1:** 

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

```

 **Example 2:** 

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

```

 **Example 3:** 

```
Input: nums = [1], target = 0
Output: -1

```

 

 **Constraints:** 

- 1 <= nums.length <= 5000
- -104 <= nums[i] <= 104
- All values of nums are unique.
- nums is an ascending array that is possibly rotated.
- -104 <= target <= 104

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.4 MB (beats 67.40%)  
**Submitted:** 2026-11-18T06:12:30.394Z  

```py
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[n - 1]:
                if target > nums[n - 1] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target > nums[mid] and target <= nums[n - 1]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1
```

---

[View on LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)