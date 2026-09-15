class Solution:
    def largest(self, arr):
        # code here
        max_ele = float('-inf')
        for num in arr:
            if num > max_ele:
                max_ele = num
        
        return max_ele
