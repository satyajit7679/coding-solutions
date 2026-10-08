class Solution:
    def segregate0and1(self, arr):
        # code here
        n = len(arr)
        i = 0
        j = n - 1
        while i < j:
            if arr[i] == 0:
                i += 1
            elif arr[j] == 1:
                j -= 1
                
            arr[i],arr[j] = arr[j],arr[i]
            
        return arr
        