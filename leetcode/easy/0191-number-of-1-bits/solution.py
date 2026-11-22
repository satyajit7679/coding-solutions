class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0

        count = 0

        while n > 0:
            count += n % 2
            n = n // 2
        
        return count