class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        ans = float('-inf')
        while i < j:
            l = j - i
            res = min(height[i],height[j]) * l
            ans = max(res,ans)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans
        