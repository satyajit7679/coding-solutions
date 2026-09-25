class Solution:
    def removeDuplicates(self, s):
        # code here
        i = 1
        res = s[0]
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                res = res + s[i]
        return res