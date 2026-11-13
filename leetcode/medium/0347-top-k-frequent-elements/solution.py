class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        res = []
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        arr = list(freq.keys())
        
        for i in range(len(arr)):
            for j in range(len(arr) - 1 - i):
                if freq[arr[j]] < freq[arr[j + 1]]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr[:k]