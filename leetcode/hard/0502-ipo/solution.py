import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:

        arr = sorted(zip(capital, profits))

        heap = []
        idx = 0
        n = len(arr)

        for _ in range(k):

            # Add all projects we can afford
            while idx < n and arr[idx][0] <= w:
                heapq.heappush(heap, -arr[idx][1])
                idx += 1

            # No project can be done
            if not heap:
                break

            # Take project with maximum profit
            pro = -heapq.heappop(heap)

            # Increase capital
            w += pro

        return w