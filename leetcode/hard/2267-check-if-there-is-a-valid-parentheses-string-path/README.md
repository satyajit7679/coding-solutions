# Check if There Is a Valid Parentheses String Path

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

A parentheses string is a  **non-empty**  string consisting only of `'('` and `')'`. It is  **valid**  if  **any**  of the following conditions is  **true** :

- It is ().
- It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
- It can be written as (A), where A is a valid parentheses string.

You are given an `m x n` matrix of parentheses `grid`. A  **valid parentheses string path**  in the grid is a path satisfying  **all**  of the following conditions:

- The path starts from the upper left cell (0, 0).
- The path ends at the bottom-right cell (m - 1, n - 1).
- The path only ever moves down or right.
- The resulting parentheses string formed by the path is valid.

Return `true`  *if there exists a  **valid parentheses string path**  in the grid.*  Otherwise, return `false`.

 

 **Example 1:** 

```
Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
Output: true
Explanation: The above diagram shows two possible paths that form valid parentheses strings.
The first path shown results in the valid parentheses string "()(())".
The second path shown results in the valid parentheses string "((()))".
Note that there may be other valid parentheses string paths.

```

 **Example 2:** 

```
Input: grid = [[")",")"],["(","("]]
Output: false
Explanation: The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.

```

 

 **Constraints:** 

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- grid[i][j] is either '(' or ')'.

## Solution

**Language:** Python  
**Runtime:** 1683 ms (beats 9.00%)  
**Memory:** 297.7 MB (beats 20.00%)  
**Submitted:** 2026-09-29T02:31:09.461Z  

```py

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # Valid parentheses string must have even length
        if (m + n - 1) % 2 != 0:
            return False

        memo = {}

        def dfs(i, j, balance):
            # Invalid balance
            if balance < 0:
                return False

            # Not enough remaining cells to close parentheses
            remaining = (m - 1 - i) + (n - 1 - j)

            if balance > remaining:
                return False

            # Destination reached
            if i == m - 1 and j == n - 1:
                return balance == 0

            # Check memoization
            if (i, j, balance) in memo:
                return memo[(i, j, balance)]

            # Move right
            right = False
            if j + 1 < n:
                new_balance = balance + (1 if grid[i][j + 1] == '(' else -1)
                right = dfs(i, j + 1, new_balance)

            # Move down
            down = False
            if i + 1 < m:
                new_balance = balance + (1 if grid[i + 1][j] == '(' else -1)
                down = dfs(i + 1, j, new_balance)

            memo[(i, j, balance)] = right or down

            return memo[(i, j, balance)]

        # Start from top-left cell
        initial = 1 if grid[0][0] == '(' else -1

        return dfs(0, 0, initial)
```

---

[View on LeetCode](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/)