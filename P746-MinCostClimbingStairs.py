class Solution:
    def minCostClimbingStairs(self, cost):
        costSoFar = [0] * (len(cost)+1)
        
        for i in range(2, len(costSoFar)):
            costSoFar[i] = min(costSoFar[i-2] + cost[i-2], costSoFar[i-1] + cost[i-1])
            
        return costSoFar[-1]