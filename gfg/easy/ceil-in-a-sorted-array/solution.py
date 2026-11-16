class Solution:
    def findCeil(self, arr, x):
        # code here
        low = 0
        high = len(arr) - 1
        res = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res