class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = nums[0]
        best_end = nums[0]
        for i in range(1,len(nums)):
            v1 = nums[i]
            v2 = nums[i] + best_end
            best_end = max(v1,v2)
            res = max(res,best_end)

        return res
        