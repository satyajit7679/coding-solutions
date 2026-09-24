class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        mul = 1
        zero = 0
        res = []

        for num in nums:
            if num == 0:
                zero += 1
            else:
                mul *= num

        for num in nums:
            if zero > 1:
                res.append(0)
            elif zero == 1:
                if num == 0:
                    res.append(mul)
                else:
                    res.append(0)
            else:
                res.append(mul // num)

        return res