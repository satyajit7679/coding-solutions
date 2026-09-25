class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def fun(nums, n, i, temp):
            if i == n:
                res.append(temp.copy())
                return

            # Don't take nums[i]
            fun(nums, n, i + 1, temp)

            # Take nums[i]
            temp.append(nums[i])
            fun(nums, n, i + 1, temp)

            # Backtrack
            temp.pop()

        fun(nums, len(nums), 0, [])

        return res