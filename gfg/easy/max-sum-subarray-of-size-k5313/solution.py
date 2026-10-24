
class Solution:
    def maxSubarraySum(self, arr, k):
        low = 0
        total = 0
        for num in range(k):
            total += arr[num]
            
        max_sum = total
        
        for high in range(k, len(arr)):
            total -= arr[low]
            low += 1
            
            total += arr[high]
            if max_sum < total:
                max_sum = total
                
        return max_sum