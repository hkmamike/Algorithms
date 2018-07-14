class Solution:
        
    def numDecodings(self, s):

        previousDigit = ''
        previousWays = 0
        
        if s > '' :
            ways = 1
        else:
            ways = 0
            
        for digit in s:
            (previousWays, 
             ways, 
             previousDigit) = (ways, 
                               (digit > '0') * ways + 
                               (9 < int(previousDigit + digit) < 27) * previousWays, 
                               digit)
            
        return ways