class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.added = set()
        candidates = sorted(candidates)
        candidates.reverse()

        def buildCombos(path, idx, remainingTarget, candidates):
            if remainingTarget < 0:
                return
            elif remainingTarget == 0:
                resultTuple = tuple(sorted(path))
                if resultTuple not in self.added:
                    self.result.append(path)
                    self.added.add(resultTuple)
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                        continue
                buildCombos(path+[candidates[i]], i+1, remainingTarget - candidates[i], candidates)

        buildCombos([], 0, target, candidates)
        return self.result