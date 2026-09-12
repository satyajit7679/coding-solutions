# Aggressive Cows

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array  **arr[]**, which denotes the positions of stalls. All the positions are distinct. There are **k**  aggressive cows.

Assign the cows to the stalls such that the **minimum**  distance between any two cows is  **maximized.** 

 **Examples:** 

```
Input: arr[] = [1, 2, 4, 8, 9], k = 3
Output: 3
Explanation: The first cow can be placed at arr[0], the second at arr[2], and the third at arr[3]. The minimum distance between any two cows is 3 (between arr[0] and arr[2]), which is the maximum possible among all valid arrangements.
```

```
Input: arr[] = [10, 1, 2, 7, 5], k = 3
Output: 4
Explanation: The first cow can be placed at arr[0], the second at arr[1], and the third at arr[4]. In this arrangement, the minimum distance between any two cows is 4 (between arr[1] and arr[4]), which is the maximum possible among all valid arrangements.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-12T17:49:46.471Z  

```py
class Solution:
    def distance(self,arr,guess,k):
        n = len(arr)
        prev = arr[0]
        cow = 1
        for i in range(1,n):
            dist = arr[i] - prev
            if dist < guess:
                continue
            
            cow += 1
            prev = arr[i]
        
            if cow >= k:
                return True
        
        return False
            
    def aggressiveCows(self, arr, k):
        # code here
        n = len(arr)
        arr.sort()
        low = 1
        high = arr[n - 1] - arr[0]
        res = -1
        while low <= high:
            guess = (low + high) // 2
            if self.distance(arr,guess,k):
                res = guess
                low = guess + 1
            else:
                high = guess - 1
                
        return res
        
        
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/aggressive-cows/1)