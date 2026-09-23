class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        target = total - x

        # If target is negative, impossible
        if target < 0:
            return -1

        left = 0
        curr = 0
        max_len = -1

        for right in range(len(nums)):
            curr += nums[right]

            # Shrink window if sum becomes too large
            while curr > target:
                curr -= nums[left]
                left += 1

            # Found a valid subarray
            if curr == target:
                max_len = max(max_len, right - left + 1)

        # No valid subarray
        if max_len == -1:
            return -1

        return len(nums) - max_len