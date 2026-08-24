class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        new_str = columnTitle.upper()
        res = 0
        for s in new_str:
            res = res * 26 + (ord(s) - ord('A') + 1)
        return res

        