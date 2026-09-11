class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        count = 0
        i = 0
        j = len(nums) - 1
        res = [0] * n
        id = 0
        while i <= j:
            if nums[i] != val:
                res[id] = nums[i]
                id += 1
                i += 1
            elif nums[j] != val:
                res[id] = nums[j]
                id += 1
                j -= 1
            elif nums[i] == val:
                i += 1
            else:
                j -= 1
            
        for i in range(n):
            nums[i] = res[i]

        return id

                
        