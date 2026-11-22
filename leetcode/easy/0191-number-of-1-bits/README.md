# Number of 1 Bits

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a positive integer `n`, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

 

Original
Python3
 **Example 1:** 

 **Input:**  n = 11

 **Output:**  3

 **Explanation:** 

The input binary string  **1011**  has a total of three set bits.

 **Example 2:** 

 **Input:**  n = 128

 **Output:**  1

 **Explanation:** 

The input binary string  **10000000**  has a total of one set bit.

 **Example 3:** 

 **Input:**  n = 2147483645

 **Output:**  30

 **Explanation:** 

The input binary string  **1111111111111111111111111111101**  has a total of thirty set bits.

 

 **Constraints:** 

- 1 <= n <= 231 - 1

 

 **Follow up:**  If this function is called many times, how would you optimize it?

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 35.86%)  
**Memory:** 19.3 MB (beats 42.09%)  
**Submitted:** 2026-11-22T10:27:45.427Z  

```py
class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0

        count = 0

        while n > 0:
            count += n % 2
            n = n // 2
        
        return count
```

---

[View on LeetCode](https://leetcode.com/problems/number-of-1-bits/)