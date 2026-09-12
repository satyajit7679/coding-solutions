# Koko Eating Bananas

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return  *the minimum integer*  `k`  *such that she can eat all the bananas within*  `h`  *hours*.

 

 **Example 1:** 

```
Input: piles = [3,6,7,11], h = 8
Output: 4

```

 **Example 2:** 

```
Input: piles = [30,11,23,4,20], h = 5
Output: 30

```

 **Example 3:** 

```
Input: piles = [30,11,23,4,20], h = 6
Output: 23

```

 

 **Constraints:** 

- 1 <= piles.length <= 104
- piles.length <= h <= 109
- 1 <= piles[i] <= 109

## Solution

**Language:** Python  
**Runtime:** 240 ms (beats 5.74%)  
**Memory:** 20.6 MB (beats 44.33%)  
**Submitted:** 2026-09-12T10:09:42.354Z  

```py
class Solution:
    def fun(self,piles,speed):
        h = 0
        n = len(piles)

        for i in range(n):
            h = h + piles[i] // speed

            if (piles[i] % speed) != 0:
                h += 1
        
        return h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high

        while low <= high:
            mid = (low + high) // 2
            k = self.fun(piles,mid)
            if k > h:
                low = mid + 1
            else:
                res = mid
                high = mid - 1
        return res        
```

---

[View on LeetCode](https://leetcode.com/problems/koko-eating-bananas/)