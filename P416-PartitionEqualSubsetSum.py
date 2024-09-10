# Add tabulation table and implement early break by returning conditionals, pass.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def find(taraget, idx, N):
            if target == 0:
                return True
            elif idx >= N or target < 0:
                return False
            elif (self.dp[idx][target] != -1):
                return self.dp[idx][target]
            self.dp[idx][target] = find(target - nums[idx], idx+1, N) or find(target, idx+1, N)
            return self.dp[idx][target]

        totalSum, N = sum(nums), len(nums)
        targetSum = totalSum // 2
        if totalSum % 2 != 0:
            return False
        else:
            self.dp = [[-1] * (targetSum + 1) for _ in range(N)]
            return find(targetSum, 0, N)

# General Solution, TLE
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False

        targetSum = totalSum // 2
        N = len(nums)
        self.solutionFound = False

        @cache
        def find(target, idx, N):
            if idx >= N or target < 0:
                return
            if target == 0:
                self.solutionFound = True
                return
            find(target - nums[idx], idx + 1, N)
            find(target, idx + 1, N)
            
        find(targetSum, 0, N)
        return self.solutionFound
