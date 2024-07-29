
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        def recurse(subTarget, candidates, attempt, idx):
            if subTarget < 0:
                return
            elif subTarget == 0:
                self.result.append(attempt)
            else:
                for i in range(idx, len(candidates)):
                    newTarget = subTarget - candidates[i]
                    newAttempt = attempt + [candidates[i]]
                    recurse(newTarget, candidates, newAttempt, i)
        
        recurse(target, candidates, [], 0)
        return self.result

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