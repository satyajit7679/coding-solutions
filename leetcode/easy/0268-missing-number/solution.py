class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        freq = {}
        for i in range(n + 1):
            freq[i] = 0
        
        for num in nums:
            freq[num] += 1

        for i in range(n + 1):
            if freq[i] == 0:
                return i

        