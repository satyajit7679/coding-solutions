class Solution:
    def distance(self,arr,guess,k):
        n = len(arr)
        prev = arr[0]
        cow = 1
        for i in range(1,n):
            dist = arr[i] - prev
            if dist < guess:
                continue
            
            cow += 1
            prev = arr[i]
        
            if cow >= k:
                return True
        
        return False
            
    def aggressiveCows(self, arr, k):
        # code here
        n = len(arr)
        arr.sort()
        low = 1
        high = arr[n - 1] - arr[0]
        res = -1
        while low <= high:
            guess = (low + high) // 2
            if self.distance(arr,guess,k):
                res = guess
                low = guess + 1
            else:
                high = guess - 1
                
        return res
        
        
        