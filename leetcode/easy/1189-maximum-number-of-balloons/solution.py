class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = "balloon"
        need = {}
        have = {}
        res = float('inf')
        for ch in s:
            need[ch] = need.get(ch,0) + 1
        for ch in text:
            have[ch] = have.get(ch,0) + 1
        for ch in need:
            ans = have.get(ch, 0) // need[ch]
            res = min(res,ans)  
        return res
        