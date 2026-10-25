# Maximum Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, find the subarray with the largest sum, and return  *its sum*.

 

 **Example 1:** 

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

```

 **Example 2:** 

```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

```

 **Example 3:** 

```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104

 

 **Follow up:**  If you have figured out the `O(n)` solution, try coding another solution using the  **divide and conquer**  approach, which is more subtle.

## Solution

**Language:** Python  
**Runtime:** 48 ms (beats 19.22%)  
**Memory:** 31.3 MB (beats 90.39%)  
**Submitted:** 2026-10-25T12:57:19.662Z  

```py
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best_end = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            v1 = best_end + nums[i]
            v2 = nums[i]
            best_end = max(v1,v2)
            ans = max(best_end,ans)
        
        return ans
        
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-subarray/)