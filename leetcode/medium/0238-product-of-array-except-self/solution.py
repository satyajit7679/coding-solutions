class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        p = 1
        s = 1
        for i in range(n):
            res[i] = p
            p = p * nums[i]

        for i in range(n - 1, -1, -1):
            res[i] = s * res[i]
            s = s * nums[i]

        return res