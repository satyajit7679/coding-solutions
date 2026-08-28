# Daily Temperatures

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of integers `temperatures` represents the daily temperatures, return  *an array*  `answer`  *such that*  `answer[i]`  *is the number of days you have to wait after the*  `ith`  *day to get a warmer temperature*. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

 

 **Example 1:** 

```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

```

 **Example 2:** 

```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

```

 **Example 3:** 

```
Input: temperatures = [30,60,90]
Output: [1,1,0]

```

 

 **Constraints:** 

- 1 <= temperatures.length <= 105
- 30 <= temperatures[i] <= 100

## Solution

**Language:** Python  
**Runtime:** 92 ms (beats 61.23%)  
**Memory:** 28.1 MB (beats 88.87%)  
**Submitted:** 2026-08-28T18:25:44.247Z  

```py
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while st and temperatures[st[-1]] <= temperatures[i]:
                st.pop()

            if st:
                ans[i] = st[-1] - i
                
            st.append(i)

        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/daily-temperatures/)