class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in nums:
            index = abs(i) - 1
            nums[index] = -abs(nums[index])
        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)
        return res