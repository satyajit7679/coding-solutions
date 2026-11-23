class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x = start ^ goal
        count = 0

        while x > 0:
            if x % 2 == 1:
                count += 1
            x = x // 2

        return count