class Solution:
    def findDisappearedNumbers(self, arr: List[int]) -> List[int]:
        freq = {}
        res = []
        n = len(arr)
        for i in range(1,n + 1):
            freq[i] = 0
        for i in range(n):
            freq[arr[i]] = 1
        for i in range(1,n + 1):
            if freq[i] == 0:
                res.append(i)
        return res