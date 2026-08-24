class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            ans1 = self.expend(s, i, i)
            ans2 = self.expend(s, i, i+1)
            if len(ans1) > len(res):
                res = ans1

            if len(ans2) > len(res):
                res = ans2
        return res

    def expend(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right] 
        