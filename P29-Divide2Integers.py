class Solution:
    def divide(self, y, x):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (y > 0) == (x > 0)
        x = abs(x)
        y = abs(y)
        result = 0

        while y >= x:
            temp, i = x, 1
            
            while y >= temp:
                y -= temp
                result += i
                i = i << 1
                temp = temp << 1

        if not positive:
            result = - result
            
        return min(max(result, -2147483648), 2147483647)
    
# Idea, TLE
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend > 0) == (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor == 1:
            if not positive:
                dividend = - dividend
            return min(max(dividend, -2147483648), 2147483647)

        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1

        if not positive:
            quotient = - quotient
        return min(max(quotient, -2147483648), 2147483647)