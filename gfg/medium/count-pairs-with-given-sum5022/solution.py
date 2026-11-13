class Solution:
    def getPairs(self, arr):
        # code here
        arr.sort()
        i = 0
        j = len(arr) - 1
        res = []
        s = 0
        
        while i < j:
            s = arr[i] + arr[j]
            if s == 0:
                res.append([arr[i],arr[j]])
                left = arr[i]
                right = arr[j]
                while i < j and arr[i] == left:
                    i += 1
                    
                while i < j and arr[j] == right:
                    j -= 1
                    
            elif s < 0:
                i += 1
            else:
                j -= 1
            
        return res