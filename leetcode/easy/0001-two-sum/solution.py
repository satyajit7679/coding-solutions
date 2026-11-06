class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        freq = {}

        for i in range(len(nums)):
            need = target - nums[i]

            if need in freq:
                return [freq[need],i]

            freq[nums[i]] = i

        return []


        