class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 1
        id = 0
        while i < len(nums):
            if nums[i] != nums[id]:
                id += 1
                nums[i],nums[id] = nums[id],nums[i]
            i += 1
        return id + 1
        