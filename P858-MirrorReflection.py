class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        
        while p % 2 == 0 and q % 2 == 0:
            p = p / 2
            q = q / 2
        
        if p % 2 == 0:
            return 2
        elif q % 2 == 0:
            return 0
        else:
            return 1