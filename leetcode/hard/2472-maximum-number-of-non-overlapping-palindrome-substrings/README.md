# Maximum Number of Non-overlapping Palindrome Substrings

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given a string `s` and a  **positive**  integer `k`.

Select a set of  **non-overlapping**  substrings from the string `s` that satisfy the following conditions:

- The length of each substring is at least k.
- Each substring is a palindrome.

Return  *the  **maximum**  number of substrings in an optimal selection*.

A  **substring**  is a contiguous sequence of characters within a string.

 

 **Example 1:** 

```
Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.

```

 **Example 2:** 

```
Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.

```

 

 **Constraints:** 

- 1 <= k <= s.length <= 2000
- s consists of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 2507 ms (beats 19.59%)  
**Memory:** 50.7 MB (beats 19.07%)  
**Submitted:** 2026-09-15T18:16:56.589Z  

```py
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        for i in range(n):
            pal[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2:
                        pal[i][j] = True
                    else:
                        pal[i][j] = pal[i + 1][j - 1]

        # dp[i] = maximum palindromes using first i characters
        dp = [0] * (n + 1)

        for i in range(n):
            # Skip s[i]
            dp[i + 1] = max(dp[i + 1], dp[i])

            # Select a palindrome starting at i
            for j in range(i + k - 1, n):
                if pal[i][j]:
                    dp[j + 1] = max(dp[j + 1], dp[i] + 1)

        return dp[n]
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/)