# class Solution:
#     def findCeil(self, arr, x):
#         # code here
#         low = 0
#         high = len(arr) - 1
#         index = -1
        
#         while low <= high:
#             mid = (low + high) // 2
#             if arr[mid] == x:
#                 return mid
            
#             if arr[mid] > x:
#                 index = mid
#                 high = mid -1
                
#             else:
#                 low = mid + 1
            
#         return index


class Solution:
    def findCeil(self, arr, x):
        low = 0
        high = len(arr) - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
