class Solution:
    def checkPerfectNumber(self, num):

        if num <= 1:
            return False
        sumVal = 1
        
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                sumVal += i
                sumVal += num//i
                
        return sumVal == num