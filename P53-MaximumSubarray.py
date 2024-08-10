class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)

        maxCandidate = 0
        maxOverall = 0

        for num in nums:
            maxCandidate += num
            maxOverall = max(maxOverall, maxCandidate)
            if maxCandidate < 0:
                maxCandidate = 0
        
        return maxOverall