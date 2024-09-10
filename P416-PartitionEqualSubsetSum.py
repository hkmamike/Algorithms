
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
