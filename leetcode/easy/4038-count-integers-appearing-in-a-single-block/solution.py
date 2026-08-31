class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        i = 1
        count = 0
        if len(nums) == 1:
            return 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                count += 1
            i += 1
        return count
        
                
        