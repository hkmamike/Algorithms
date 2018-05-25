class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        valuesMap = {}
        count = 0
        
        for a in A:
            for b in B:
                value = a + b
                
                if value in valuesMap:
                    valuesMap[value] += 1
                else:
                    valuesMap[value] = 1
                    
        for c in C:
            for d in D:
                target = - (c + d)
                
                if target in valuesMap:
                    count += valuesMap[target]
                        
        return count
        