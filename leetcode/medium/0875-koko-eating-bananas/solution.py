class Solution:
    def fun(self,piles,speed):
        h = 0
        n = len(piles)

        for i in range(n):
            h = h + piles[i] // speed

            if (piles[i] % speed) != 0:
                h += 1
        
        return h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high

        while low <= high:
            mid = (low + high) // 2
            k = self.fun(piles,mid)
            if k > h:
                low = mid + 1
            else:
                res = mid
                high = mid - 1
        return res        