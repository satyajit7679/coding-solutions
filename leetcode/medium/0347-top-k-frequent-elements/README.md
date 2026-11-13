# Top K Frequent Elements

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums` and an integer `k`, return  *the*  `k`  *most frequent elements*. You may return the answer in  **any order**.

 

Original
Python3
 **Example 1:** 

 **Input:**  nums = [1,1,1,2,2,3], k = 2

 **Output:**  [1,2]

 **Example 2:** 

 **Input:**  nums = [1], k = 1

 **Output:**  [1]

 **Example 3:** 

 **Input:**  nums = [1,2,1,2,1,2,3,1,3,2], k = 2

 **Output:**  [1,2]

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

 

 **Follow up:**  Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

## Solution

**Language:** Python  
**Runtime:** 357 ms (beats 5.13%)  
**Memory:** 22.5 MB (beats 99.41%)  
**Submitted:** 2026-11-13T05:22:54.714Z  

```py
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        res = []
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        arr = list(freq.keys())
        
        for i in range(len(arr)):
            for j in range(len(arr) - 1 - i):
                if freq[arr[j]] < freq[arr[j + 1]]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr[:k]
```

---

[View on LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)