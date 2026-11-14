class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        j = n - 1
        ans = 0
        i = 0
        while i < j:
            h = min(height[i],height[j])
            l = j - i
            res = h * l
            ans = max(res,ans)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return ans

        