class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        res = 0
        odd = False
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        for ch in freq:
            val = freq[ch]
            if val % 2 == 0:
                res += val
            else:
                res += val - 1
                odd = True
        
        if odd:
            res += 1
        
        return res
        

        