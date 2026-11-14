# Container With Most Water

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return  *the maximum amount of water a container can store*.

 **Notice**  that you may not slant the container.

 

Original
Python3
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
**Runtime:** 60 ms (beats 39.55%)  
**Memory:** 29.6 MB (beats 39.12%)  
**Submitted:** 2026-11-14T17:45:18.735Z  

```py
class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        j = n - 1
        ans = 0
        i = 0
        while i < j:
            h = min(height[i],height[j])
            l = j - i
            res = h * l
            ans = max(res,ans)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return ans

        
```

---

[View on LeetCode](https://leetcode.com/problems/container-with-most-water/)