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