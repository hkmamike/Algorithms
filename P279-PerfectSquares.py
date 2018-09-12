import math

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        sqs = []
        i = 1
        while i*i <= n:
            sqs.append(i*i)
            i+=1
        count = 0
        toCheck = {n}
        
        while toCheck:
            count += 1
            temp = set()
            for x in toCheck:
                for y in sqs:
                    if x==y:
                        return count
                    elif x < y:
                        break
                    temp.add(x-y)
            toCheck = temp
            
        return count
            