class Solution:
    def count_non_minimum(self, nums):
        # write your code here
        min_value = min(nums)
        count = 0
        for i in range(len(nums)):
            if nums[i] != min_value:
                count += 1
        return count
        
