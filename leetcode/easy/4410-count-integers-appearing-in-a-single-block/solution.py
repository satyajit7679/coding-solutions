class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        f = {}
        l = {}
        freq = {}
        for i,x in enumerate(nums):
            if x not in f:
                f[x] = i
            l[x] = i
            freq[x] = freq.get(x,0) + 1
        c = 0

        for x in f:
            length = l[x] - f[x] + 1

            if length == freq[x]:
                c += 1
        return c
        
                
        