# Array Leaders

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an array  **`arr`**  of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.

**Examples:
**

```
Input: arr = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.

```

```
Input: arr = [10, 4, 2, 4, 1]
Output: [10, 4, 4, 1]
Explanation: Note that both of the 4s are in output, as to be a leader an equal element is also allowed on the right. side
```

```
Input: arr = [5, 10, 20, 40]
Output: [40]
Explanation: When an array is sorted in increasing order, only the rightmost element is leader.
```

```
Input: arr = [30, 10, 10, 5]
Output: [30, 10, 10, 5]
Explanation: When an array is sorted in non-increasing order, all elements are leaders.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-16T09:33:34.201Z  

```py
class Solution:
    def leaders(self, arr):
        # code here
        i = len(arr) - 2
		id = len(arr) - 1
		res = []
		res.append(arr[id])
		while i >= 0:
			if arr[i] >= arr[id]:
				res.append(arr[i])
				id = i
				i -= 1
			else:
			    i -= 1
		res.reverse()
		
		return res
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1)