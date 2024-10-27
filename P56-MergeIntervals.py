# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for i, entry in enumerate(intervals):
            if i == 0: continue

            if entry[0] <= result[-1][1]:
                start = result[-1][0]
                end = max(entry[1], result[-1][1])
                result.pop()
                result.append([start, end])
            else:
                result.append(entry)

        return result

class Solution:
    def merge(self, intervals):
        
        if not intervals:
            return []
        
        intervals = sorted(intervals, key=lambda x: x.start)
        results = [intervals[0]]

        for interval in intervals[1:]:
            
            if interval.start <= results[-1].end:
                results[-1].end = max(interval.end, results[-1].end)
            else:
                results.append(interval)
                
        return results