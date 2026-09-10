class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            # find which part of my mid
            #  if True then part 1
            if nums[mid] > nums[n-1]: 
                if nums[mid] < target:
                    low = mid + 1
                else:
                    if nums[0] > target:
                        low = mid + 1
                    else:
                        high = mid - 1
                continue
            # part 2
            
            if nums[mid] > target:
                high = mid - 1
            else:
                if nums[n-1] < target:
                    high = mid - 1
                else:
                    low = mid + 1
        
        return -1 






        return -1