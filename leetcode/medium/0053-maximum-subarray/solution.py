class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best_end = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            v1 = best_end + nums[i]
            v2 = nums[i]
            best_end = max(v1,v2)
            ans = max(best_end,ans)
        
        return ans
        