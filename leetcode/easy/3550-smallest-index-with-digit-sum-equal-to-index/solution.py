class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sumDigit(num):
            s = 0
            while num > 0:
                r = num % 10
                s = s + r
                num = num // 10
            return s

        for i in range(len(nums)):
            ans = sumDigit(nums[i])
            if ans == i:
                return i
        return -1 

        