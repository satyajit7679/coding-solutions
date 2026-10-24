class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        max_len = 0
        low = 0
        freq = {}
        l = 0
        for high in range(len(fruits)):
            freq[fruits[high]] = freq.get(fruits[high],0) + 1
            while len(freq) > 2:
                freq[fruits[low]] -= 1
                if freq[fruits[low]] == 0:
                    del freq[fruits[low]]
                low += 1

            l = high - low + 1
            max_len = max(max_len,l)

        return max_len

        