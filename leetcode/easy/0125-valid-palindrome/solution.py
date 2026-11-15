class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        for ch in s:
            if ch.isalnum():
                r += ch.lower()
        
        i = 0
        j = len(r) - 1
        while i < j:
            if r[i] != r[j]:
                return False
            i += 1
            j -= 1

        return True
            