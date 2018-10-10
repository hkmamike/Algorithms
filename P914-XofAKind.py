class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        count = {}
        for card in deck:
            if card in count:
                count[card] += 1
            else:
                count[card] = 1
        
        count = count.values()
        
        return reduce(gcd, count) > 1