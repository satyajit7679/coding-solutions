# Insert Interval

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [starti, endi]` represent the start and the end of the `ith` interval and `intervals` is sorted in ascending order by `starti`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Two intervals are considered overlapping if they share  **at least**  one point.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `starti` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` *after the insertion*.

 **Note**  that you don't need to modify `intervals` in-place. You can make a new array and return it.

 

 **Example 1:** 

```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

```

 **Example 2:** 

```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

```

 

 **Constraints:** 

- 0 <= intervals.length <= 104
- intervals[i].length == 2
- 0 <= starti <= endi <= 105
- intervals is sorted by starti in ascending order.
- newInterval.length == 2
- 0 <= start <= end <= 105

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 21.5 MB (beats 26.88%)  
**Submitted:** 2026-08-24T15:02:42.967Z  

```py
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        insert = False

        for i in range(len(intervals)):
            s2 = intervals[i][0]
            e2 = intervals[i][1]

            if newInterval[0] < s2:
                if insert == False:
                    res.append(newInterval)
                    insert = True
                res.append(intervals[i])
            else:
                res.append(intervals[i])

        if insert == False:
            res.append(newInterval)

        return self.merge_interval(res)

    def merge_interval(self, arr):
        s1 = arr[0][0]
        e1 = arr[0][1]
        res = []

        for i in range(1, len(arr)):
            s2 = arr[i][0]
            e2 = arr[i][1]

            if e1 >= s2:
                s1 = s1
                e1 = max(e1, e2)
                continue

            res.append([s1, e1])
            s1 = s2
            e1 = e2

        res.append([s1, e1])
        return res
```

---

[View on LeetCode](https://leetcode.com/problems/insert-interval/)