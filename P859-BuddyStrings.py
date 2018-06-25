class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        switch = []
        dupCheck = set()
        dupFlag = False
        
        for i in range(len(A)):
            if A[i] != B[i]:
                switch.append(i)
            elif A[i] in dupCheck:
                dupFlag = 1
            else:
                dupCheck.add(A[i])
        
        if len(switch) == 0 and dupFlag:
            return True
        elif len(switch) ==0:
            return False
        elif len(switch) == 2:
            
            A = list(A)
            A[switch[0]], A[switch[1]] = A[switch[1]], A[switch[0]]
            A = ''.join(A)
            
        else:
            return False
        
        return A == B