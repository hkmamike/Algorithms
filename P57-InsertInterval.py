class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
        left = [i for i in intervals if i[1] < newInterval[0]]
        right = [i for i in intervals if i[0] > newInterval[1]]

        if left + right != intervals:
            start = min(start, intervals[len(left)][0])
            end = max(end, intervals[len(intervals) - len(right) - 1][1])

        return left + [[start, end]] + right
