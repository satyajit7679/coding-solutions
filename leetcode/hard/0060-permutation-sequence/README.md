# Permutation Sequence

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

The set `[1, 2, 3,..., n]` contains a total of `n!` unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for `n = 3`:

- "123"
- "132"
- "213"
- "231"
- "312"
- "321"

Given `n` and `k`, return the `kth` permutation sequence.

 

 **Example 1:** 

```
Input: n = 3, k = 3
Output: "213"

```

 **Example 2:** 

```
Input: n = 4, k = 9
Output: "2314"

```

 **Example 3:** 

```
Input: n = 3, k = 1
Output: "123"

```

 

 **Constraints:** 

- 1 <= n <= 9
- 1 <= k <= n!

## Solution

**Language:** Python  
**Runtime:** 4 ms (beats 13.17%)  
**Memory:** 19.2 MB (beats 97.64%)  
**Submitted:** 2026-09-06T18:20:11.675Z  

```py
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]

        factorial = 1
        for i in range(1, n):
            factorial *= i

        k -= 1

        result = []

        for i in range(n - 1, -1, -1):

            index = k // factorial

            result.append(numbers[index])

            numbers.pop(index)

            if i > 0:
                k = k % factorial
                factorial = factorial // i

        return ''.join(result)
```

---

[View on LeetCode](https://leetcode.com/problems/permutation-sequence/)