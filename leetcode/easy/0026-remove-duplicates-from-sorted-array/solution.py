class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        id = 0
        while i <= len(nums) - 1:
            if nums[i] != nums[id]:
                id +=1
                nums[id],nums[i] = nums[i],nums[id]
            i += 1
        
        return id + 1
         