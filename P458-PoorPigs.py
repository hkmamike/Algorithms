class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        rounds = (minutesToTest // minutesToDie + 1)
        
        p = 0
        while rounds**p < buckets:
            p += 1
            
        return p 
        