class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = 0
        low = 0
        max_len = 0
        l = 0
        freq = {}
        for high in range(len(s)):
            freq[s[high]] = freq.get(s[high],0) + 1
            k = high - low + 1
            while len(freq) < k:
                freq[s[low]] -= 1
                if freq[s[low]] == 0:
                    del freq[s[low]]
                low += 1
                k = high - low + 1

            l = high - low + 1
            max_len = max(max_len,l)

        return max_len 
        