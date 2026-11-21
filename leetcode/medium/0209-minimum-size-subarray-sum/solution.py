class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        low = 0
        min_len = float('inf')
        t = 0
        for high in range(len(nums)):
            t += nums[high]
            while t >= target:
                l = high - low + 1
                min_len = min(l,min_len)
                t -= nums[low]
                low += 1
        
        if min_len == float('inf'):
            return 0
        
        return min_len
        