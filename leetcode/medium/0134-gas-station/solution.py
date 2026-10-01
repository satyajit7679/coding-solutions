class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        start = 0
        curGas = 0
        totalGas = 0
        totalCost = 0

        for i in range(len(gas)):
            totalGas += gas[i]
            totalCost += cost[i]
            curGas += (gas[i] - cost[i])

            if curGas < 0:
                start = i + 1
                curGas = 0

        
        if totalGas < totalCost:
            return -1
        else:
            return start
        