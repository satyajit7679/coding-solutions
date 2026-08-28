# Container With Most Water

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return  *the maximum amount of water a container can store*.

 **Notice**  that you may not slant the container.

 

 **Example 1:** 

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

```

 **Example 2:** 

```
Input: height = [1,1]
Output: 1

```

 

 **Constraints:** 

- n == height.length
- 2 <= n <= 105
- 0 <= height[i] <= 104

## Solution

**Language:** Python  
**Runtime:** 63 ms (beats 26.30%)  
**Memory:** 29.5 MB (beats 67.57%)  
**Submitted:** 2026-08-27T18:12:14.060Z  

```py
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        ans = 0
        while i < j:
            width = j - i
            area = min(height[i],height[j]) * width
            ans = max(area,ans)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans
        
```

---

[View on LeetCode](https://leetcode.com/problems/container-with-most-water/)