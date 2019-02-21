class Solution:
    def pancakeSort(self, A: 'List[int]') -> 'List[int]':
        
        result = []
        for i in range (len(A), 1, -1):
            maxIndex = A.index(max(A[:i]))
            result.extend([maxIndex+1, i])
            A = A[:maxIndex:-1] + A[:maxIndex]

        return result
            