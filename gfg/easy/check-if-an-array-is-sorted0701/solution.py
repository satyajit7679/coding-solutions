class Solution:
    def isSorted(self, arr):
        # code here
        return self.fun(arr,0,len(arr))    
        
    def fun(self,arr,i,n):
        if i >= n - 1:
            return True
        
        
        if arr[i] > arr[i+1]:
            return False
            
        return self.fun(arr,i+1,n)
