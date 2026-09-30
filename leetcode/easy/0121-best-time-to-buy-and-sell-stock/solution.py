class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        buy = arr[0]
        res = 0
        for i in range(1,len(arr)):
            if arr[i] < buy:
                buy = arr[i]
            profit = arr[i] - buy
            res = max(res,profit)
        return res