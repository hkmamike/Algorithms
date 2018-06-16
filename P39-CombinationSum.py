class Solution:
    
    resultsList = []
    
    def helper(self, candidates, testCase, target, index):
        if target < 0:
            pass
        elif target == 0:
            self.resultsList.append(testCase)
        else:
            for i in range (index, len(candidates)):
                newTestCase = testCase + [candidates[i]]
                self.helper(candidates, newTestCase, target - candidates[i], i)
    
    def combinationSum(self, candidates, target):
        
        self.resultsList = []
        testCase = []
        self.helper(candidates, testCase, target, 0)
        
        return self.resultsList