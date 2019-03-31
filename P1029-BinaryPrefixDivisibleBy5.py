class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        
        value = A[0]
        result = [value % 5 == 0]
        
        for i in range(1, len(A)):
            value = value * 2 + A[i]
            result.append(value % 5 == 0)
            
        return result