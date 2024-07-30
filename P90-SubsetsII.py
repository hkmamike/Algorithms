class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.added = set()

        def buildCandidates(candidate, idx, nums):
            if idx == len(nums):
                candidateTuple = tuple(sorted(candidate))
                if candidateTuple not in self.added:
                    self.added.add(candidateTuple)
                    self.result.append(candidate)
            else:
                newCandidate = candidate.copy() + [nums[idx]]
                buildCandidates(candidate, idx + 1, nums)
                buildCandidates(newCandidate, idx + 1, nums)

        buildCandidates([], 0, nums)
        return self.result

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