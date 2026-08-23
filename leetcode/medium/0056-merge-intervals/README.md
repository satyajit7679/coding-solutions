# Merge Intervals

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return  *an array of the non-overlapping intervals that cover all the intervals in the input*.

 

 **Example 1:** 

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

```

 **Example 2:** 

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

```

 **Example 3:** 

```
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.

```

 

 **Constraints:** 

- 1 <= intervals.length <= 104
- intervals[i].length == 2
- 0 <= starti <= endi <= 104

## Solution

**Language:** Python  
**Runtime:** 10 ms (beats 29.44%)  
**Memory:** 23.2 MB (beats 28.30%)  
**Submitted:** 2026-08-23T14:59:49.759Z  

```py
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        s1 = intervals[0][0]
        e1 = intervals[0][1]
        for i in range(len(intervals)):
            s2 = intervals[i][0]
            e2 = intervals[i][1]
            if e1 >= s2:
                s1 = s1
                e1 = max(e1,e2)
                continue
            res.append([s1,e1])
            s1 = s2
            e1 = e2
        res.append([s1,e1])
        return res
        
```

---

[View on LeetCode](https://leetcode.com/problems/merge-intervals/)