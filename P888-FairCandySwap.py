class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        setA = set(A)
        sumA = sum(A)
        sumB = sum(B)
        diff = sumB - sumA
        
        for candy in B:
            targetA = candy - (diff)/2
            
            if targetA in setA:
                return [targetA, candy]
