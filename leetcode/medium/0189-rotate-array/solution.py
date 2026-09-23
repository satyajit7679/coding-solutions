class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseNums(nums,low,high):
            while low < high:
                nums[low],nums[high] = nums[high],nums[low]
                low += 1
                high -= 1
            return nums

        n = len(nums)
        k = k % n

        reverseNums(nums,0,n - 1)
        reverseNums(nums,0,k - 1)
        reverseNums(nums,k,n - 1)
        
        