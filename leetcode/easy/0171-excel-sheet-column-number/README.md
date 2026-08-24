# Excel Sheet Column Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `columnTitle` that represents the column title as appears in an Excel sheet, return  *its corresponding column number*.

For example:

```
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

```

 

 **Example 1:** 

```
Input: columnTitle = "A"
Output: 1

```

 **Example 2:** 

```
Input: columnTitle = "AB"
Output: 28

```

 **Example 3:** 

```
Input: columnTitle = "ZY"
Output: 701

```

 

 **Constraints:** 

- 1 <= columnTitle.length <= 7
- columnTitle consists only of uppercase English letters.
- columnTitle is in the range ["A", "FXSHRXW"].

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.2 MB (beats 83.37%)  
**Submitted:** 2026-08-24T15:25:40.972Z  

```py
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for s in columnTitle:
            res = res * 26 + (ord(s) - ord('A') + 1)
        return res

        
```

---

[View on LeetCode](https://leetcode.com/problems/excel-sheet-column-number/)