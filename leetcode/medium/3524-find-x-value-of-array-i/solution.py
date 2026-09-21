class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        result = [0] * k

        # dp[r] = number of subarrays ending at previous index
        # whose product % k == r
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Start a new subarray with only num
            r = num % k
            new_dp[r] += 1

            # Extend all previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * num) % k
                    new_dp[new_r] += dp[r]

            # Add all subarrays ending at current position
            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result