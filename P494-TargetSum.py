class Solution:
    def findTargetSumWays(self, nums, S):
        def recurseHelper(S, i):
            if (S, i) not in cache:
                count = 0
                
                if i == len(nums):
                    if S == 0:
                        count = 1
                else:
                    count = recurseHelper(S + nums[i], i+1) + recurseHelper(S - nums[i], i+1)
                    
                cache[(S, i)] = count
                    
            return cache[(S, i)]

        cache = {}
        return recurseHelper(S, 0)