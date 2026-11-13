# Pairs with 0 Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array  **arr**, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.

Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.

 **Examples:** 

```
Input: arr = [-1, 0, 1, 2, -1, -4]
Output: [[-1, 1]]
Explanation: arr[0] + arr[2] = (-1)+ 1 = 0.
arr[2] + arr[4] = 1 + (-1) = 0.
The distinct pair are [-1,1].

```

```
Input: arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
Output: [[-6, 6],[-1, 1]]
Explanation: The distinct pairs are [-1, 1] and [-6, 6].
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-13T07:31:27.566Z  

```py
class Solution:
    def getPairs(self, arr):
        # code here
        arr.sort()
        i = 0
        j = len(arr) - 1
        res = []
        s = 0
        
        while i < j:
            s = arr[i] + arr[j]
            if s == 0:
                res.append([arr[i],arr[j]])
                left = arr[i]
                right = arr[j]
                while i < j and arr[i] == left:
                    i += 1
                    
                while i < j and arr[j] == right:
                    j -= 1
                    
            elif s < 0:
                i += 1
            else:
                j -= 1
            
        return res
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1)