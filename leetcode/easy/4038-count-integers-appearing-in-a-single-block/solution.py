class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        i = 0
        count = 0
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                count += 1
            i += 1
        return count
        
                
        