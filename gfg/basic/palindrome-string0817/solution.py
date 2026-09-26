class Solution:
    def isPalindrome(self, s):
        # code here
        def fun(s,high,low):
            l = high - low + 1
            if l == 0 or l == 1:
                return True
                
            if s[low] != s[high]:
                return False
                
            return fun(s,high - 1, low + 1)
            
        n = len(s)
        return fun(s, n - 1, 0)
