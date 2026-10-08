class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        i = 0
        j = n - 1
        while i < j:
            total = numbers[i] + numbers[j]
            if total == target:
                return i + 1,j + 1
            if total > target:
                j -= 1
            else:
                i += 1
        return -1
        