class Solution:
    def isRectangleOverlap(self, r1, r2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if r1[0] > r2[0]:
            r1, r2 = r2, r1
            
        if r1[2] <= r2[0] or r1[3] <= r2[1]:
            return False
        
        return r1[1] < r2[3]