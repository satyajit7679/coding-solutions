class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        low = 0
        t = 0
        min_len = float('inf')
        for high in range(len(nums)):
            t += nums[high]
            while t >= target:
                l = high - low + 1
                min_len = min(l,min_len)
                t -= nums[low]
                low += 1
        return 0 if min_len == float('inf') else min_len

        