class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] < nums[mid + 1]:
                # Going uphill → peak is on the right
                low = mid + 1
            else:
                # Going downhill → peak is at mid or on the left
                high = mid

        return low
        