class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        s = 0
        for i in range(len(nums)):
            s += nums[i]

        t = 0
        for i in range(n + 1):
            t += i

        return (t - s)

        