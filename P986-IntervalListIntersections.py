# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        h = []

        for entry in firstList:
            heappush(h, entry)
        for entry in secondList:
            heappush(h, entry)

        currentJob = heappop(h)
        currentEnd = currentJob[1]
        result = []

        while h:
            entry = heappop(h)
            if entry[0] > currentEnd:
                currentEnd = entry[1]

            elif entry[1] > currentEnd:
                result.append([entry[0], currentEnd])
                currentEnd = entry[1]
            else:
                result.append([entry[0], entry[1]])
        
        return result

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        A_index = 0
        B_index = 0
        
        while A_index < len(A) and B_index < len(B):
            if A[A_index].start > B[B_index].end:
                B_index += 1
            elif B[B_index].start > A[A_index].end:
                A_index += 1
            else:
                intervalStart = max(B[B_index].start, A[A_index].start)
                intervalEnd = min(B[B_index].end, A[A_index].end)
                result.append(Interval(intervalStart, intervalEnd))
                
                if B[B_index].end == A[A_index].end:
                    B_index += 1
                    A_index += 1
                elif B[B_index].end > A[A_index].end:
                    A_index += 1
                else:
                    B_index += 1
                    
        return result