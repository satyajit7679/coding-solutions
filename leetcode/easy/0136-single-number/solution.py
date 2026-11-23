class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        x = 0

        for i in range(len(nums)):
            x = x ^ nums[i]

        return x