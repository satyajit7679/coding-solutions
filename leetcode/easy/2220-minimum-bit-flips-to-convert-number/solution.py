class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        def decimalToBinary(num):
            bit = []
            while num != 0:
                r = num % 2
                bit.append(str(r))
                num = num // 2

            bit.reverse()
            return "".join(bit)

        n1 = decimalToBinary(start)
        n2 = decimalToBinary(goal)

        n = max(len(n1), len(n2))

        n1 = n1.zfill(n)
        n2 = n2.zfill(n)

        count = 0

        for i in range(n):
            if n1[i] != n2[i]:
                count += 1

        return count