class Solution:
    def getSecondLargest(self, arr):
        # code here
        l = arr[0]
        sl = -1
        for i in range(1,len(arr)):
            if arr[i] > l:
                sl = l
                l = arr[i]
            if arr[i] > sl and arr[i] < l:
                sl = arr[i]
        
        return sl
                