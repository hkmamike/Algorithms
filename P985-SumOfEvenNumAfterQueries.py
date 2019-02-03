class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        results = []
        evenSum = 0
        
        for a in A:
            if a % 2 == 0:
                evenSum += a
                
        for query in queries:
            indexToChange = query[1]
            valueToAdd = query[0]
            
            if A[indexToChange] % 2 == 0:
                evenSum -= A[indexToChange]
                
            A[indexToChange] += valueToAdd
            
            if A[indexToChange] % 2 == 0:
                evenSum += A[indexToChange]
                
            results.append(evenSum)
            
        return results
        
        