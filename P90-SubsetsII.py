class Solution:

    results = []
    
    def recurseHelper(self, nums, index, candidate):
        
        if index == len(nums) and candidate not in self.results:
            self.results.append(candidate)
        elif index != len(nums):
            newCandidate1 = candidate.copy()
            newCandidate1.append(nums[index])
            newCandidate2 = candidate.copy()
            self.recurseHelper(nums, index+1, newCandidate1)
            self.recurseHelper(nums, index+1, newCandidate2)
    
    
    def subsetsWithDup(self, nums):
        
        self.results = []
        
        nums = sorted(nums)
        self.recurseHelper(nums, 0, [])
        return self.results