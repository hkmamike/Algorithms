class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        currentEndTime = float('-inf')
        erased = 0
        for i in sorted(intervals, key=lambda x: x[1]):
            if i[0] >= currentEndTime:
                currentEndTime = i[1]
            else:
                erased += 1
        return erased