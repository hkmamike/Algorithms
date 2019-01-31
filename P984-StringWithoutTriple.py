class Solution:
    def strWithout3a3b(self, A, B):

        result = []
        currentChar = 'a' if A > B else 'b'
        
        while A + B > 0:
            if currentChar == 'a':
                result.append('aa' if A > B and A > 1 else 'a')
                A -= 2 if A > B and A > 1 else 1
                currentChar = 'b'
                
            else:
                result.append('bb' if B > A and B > 1 else 'b')
                B -= 2 if B > A and B > 1 else 1
                currentChar = 'a'
                
        return "".join(result)
        