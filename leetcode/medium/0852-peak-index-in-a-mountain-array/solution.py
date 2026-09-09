class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1
        res = -1
        while low <= high:
            peak = (low + high) // 2
            if arr[peak] < arr[peak + 1]:
                low = peak + 1
            else:
                res = peak
                high = peak - 1
        
        return res

        