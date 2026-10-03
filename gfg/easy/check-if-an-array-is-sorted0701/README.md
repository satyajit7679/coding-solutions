# Check Sorted Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array  **arr[]**, check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.

 **Examples:** 

```
Input: arr[] = [10, 20, 30, 40, 50]
Output: true
Explanation: The given array is sorted.
```

```
Input: arr[] = [90, 80, 100, 70, 40, 30]
Output: false
Explanation: The given array is not sorted.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-03T11:15:04.727Z  

```py
class Solution:
    def isSorted(self, arr):
        # code here
        return self.fun(arr,0,len(arr))    
        
    def fun(self,arr,i,n):
        if i >= n - 1:
            return True
        
        
        if arr[i] > arr[i+1]:
            return False
            
        return self.fun(arr,i+1,n)

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1)