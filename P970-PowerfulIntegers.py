class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        powerfulIntegers = set()
        
        iRange = [i for i in range(20) if x**i < bound]
        jRange = [j for j in range(20) if y**j < bound]
        
        for i in iRange:
            for j in jRange:
                c = x**i + y**j
                if c <= bound:
                    powerfulIntegers.add(c)
                else:
                    break
                    
        return [x for x in powerfulIntegers]
        
        