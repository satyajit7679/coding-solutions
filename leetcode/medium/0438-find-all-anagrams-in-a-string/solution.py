class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        res = []
        f = {}
        w = {}
        low = 0
        for ch in p:
            f[ch] = f.get(ch,0) + 1

        for high in range(len(s)):
            w[s[high]] = w.get(s[high],0) + 1

            if high - low + 1 > len(p):
                w[s[low]] -= 1

                if w[s[low]] == 0:
                    del w[s[low]]

                low += 1

            if w == f:
                res.append(low)

        return res

        