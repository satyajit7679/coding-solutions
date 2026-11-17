class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1
        res = 0
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                res = nums[mid]
                low = mid + 1
            else:
                high = mid - 1

        return res