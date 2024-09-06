class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0, 1]
        previous = ""
        for i, c in enumerate(s):
            dp.append(dp[-1] * (c > "0") + dp[-2] * (9 < int(previous + c) < 27))
            previous = c
        
        return dp[-1]


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