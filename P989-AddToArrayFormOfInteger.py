class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        KArrayChar = list(str(K))
        KArray = [int(x) for x in KArrayChar]
        
        resultReversed = []
        carry = 0
        
        while KArray or A:
            digitSum = carry
            if KArray:
                digitSum += KArray.pop()
            if A:
                digitSum += A.pop()

            digit = digitSum % 10
            carry = digitSum // 10
            
            resultReversed.append(digit)
            
        if carry:
            resultReversed.append(1)
            
        return resultReversed[::-1]
        
        