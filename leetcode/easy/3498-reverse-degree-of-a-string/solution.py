class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            v = ord('z') - ord(s[i]) + 1
            total += (v * (i + 1))

        return total
        