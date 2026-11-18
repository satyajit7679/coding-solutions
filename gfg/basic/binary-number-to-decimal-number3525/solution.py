
class Solution:
    def binaryToDecimal(self, b):
        b = int(b)
        p = 0
        ans = 0

        while b != 0:
            r = b % 10
            ans = ans + (r * (2 ** p))
            p += 1
            b = b // 10

        return ans
