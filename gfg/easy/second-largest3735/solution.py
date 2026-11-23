class Solution:
    def getSecondLargest(self, arr):
        # code here
        s_max = -1
        max_ele = -1
        for i in range(len(arr)):
            if arr[i] > max_ele:
                s_max = max_ele
                max_ele = arr[i]
            
            if arr[i] != max_ele and arr[i] > s_max:
                s_max = arr[i]
                
        return s_max