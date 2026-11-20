class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        id = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[id],nums[i] = nums[i],nums[id]
                id += 1
            
            i += 1
        
        return nums
        