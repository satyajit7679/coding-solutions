# Reorganize String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same.

Return  *any possible rearrangement of*  `s`  *or return*  `""`  *if not possible*.

 

 **Example 1:** 

```
Input: s = "aab"
Output: "aba"

```

 **Example 2:** 

```
Input: s = "aaab"
Output: ""

```

 

 **Constraints:** 

- 1 <= s.length <= 500
- s consists of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 51.51%)  
**Memory:** 19.4 MB (beats 54.14%)  
**Submitted:** 2026-09-19T05:00:52.938Z  

```py
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1

         # Check if rearrangement is impossible
        if max(freq.values()) > (len(s) + 1) // 2:
            return ""

        heap = []
        
        for ch,count in freq.items():
            heapq.heappush(heap,(-count,ch))

        ans = []
        prev_count = 0
        prev_ch = ""

        while heap:
            count,ch = heapq.heappop(heap)
            if ch == prev_ch:
                if not heap:
                    return ""
                count2,ch2 = heapq.heappop(heap)
                ans.append(ch2)
                count2 += 1
                heapq.heappush(heap,(count,ch))
                prev_ch = ch2
                prev_count = count2
            else:
                ans.append(ch)
                count += 1
                if prev_count < 0:
                    heapq.heappush(heap,(prev_count,prev_ch))
                prev_ch = ch
                prev_count = count

        return "".join(ans)

        
```

---

[View on LeetCode](https://leetcode.com/problems/reorganize-string/)