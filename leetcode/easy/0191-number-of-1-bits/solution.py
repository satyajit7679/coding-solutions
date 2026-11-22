class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        b = []
        while n > 0:
            b.append(str(n % 2))
            n = n // 2

        
        count = 0
        for i in range(len(b)):
            if b[i] == "1":
                count += 1
        
        return count