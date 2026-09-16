# Kth Largest Element in an Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums` and an integer `k`, return  *the*  `kth`  *largest element in the array*.

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

Can you solve it without sorting?

 

 **Example 1:** 

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

```

 **Example 2:** 

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

```

 

 **Constraints:** 

- 1 <= k <= nums.length <= 105
- -104 <= nums[i] <= 104

## Solution

**Language:** Python  
**Runtime:** 109 ms (beats 27.33%)  
**Memory:** 30.9 MB (beats 86.34%)  
**Submitted:** 2026-09-16T15:18:33.651Z  

```py
import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for x in nums:
            heapq.heappush(heap,x)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
        
```

---

[View on LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/)