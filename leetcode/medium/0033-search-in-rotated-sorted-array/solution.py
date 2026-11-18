class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[n - 1]:
                if target > nums[n - 1] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target > nums[mid] and target <= nums[n - 1]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1