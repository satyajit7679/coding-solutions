class Solution:
    def longestKSubstr(self, s, k):
        # code here
        low = 0
        freq = {}
        max_len = -float('inf')
        for high in range(len(s)):
            freq[s[high]] = freq.get(s[high],0) + 1
            while len(freq) > k:
                freq[s[low]] -= 1
                if freq[s[low]] == 0:
                    del freq[s[low]]
                low += 1
                
            if len(freq) == k:
                l = high - low + 1
                max_len = max(max_len,l)
                    
        return -1 if max_len == -float('inf') else max_len                    
        