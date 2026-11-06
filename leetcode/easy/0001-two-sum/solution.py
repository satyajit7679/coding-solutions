class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 0 
        j = len(nums) - 1
        while i <= j:
            s = nums[i] + nums[j]
            if s < target:
                i += 1
            else:
                j -= 1

        return [i,j+1]

            
        