class Solution:
    def convertToBase7(self, n):
        """
        :type num: int
        :rtype: str
        """
        neg = (n < 0)
        n = abs(n)
        s = ""
        
        while n >= 0:
            s += str(n%7)
            n = n//7
            print(s, n)
            if n == 0:
                    break
                    
        return neg*'-'+s[::-1]
            