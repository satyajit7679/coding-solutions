class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            
        total = 0

        for i in range(len(nums)):
            rem = s - nums[i]

            if rem % 2 == 0:
                t = rem // 2

                if total == t:
                    return i

            total += nums[i]

        return -1