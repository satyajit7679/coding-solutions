class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        t = 0
        for i in range(k):
            t += arr[i]
        i = 0
        max_t = t
        for j in range(k,len(arr)):
            t = t - arr[i] + arr[j]
            if max_t < t:
                max_t = t
            i += 1
        return max_t