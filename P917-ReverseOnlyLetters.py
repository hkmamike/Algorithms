class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        def swap(l, r, S):
            S[l], S[r] = S[r], S[l]
            
        def getNextPair(left, right, S):
            while left < len(S) and not S[left].isalpha():
                left += 1
            
            while right >= 0 and not S[right].isalpha():
                right -= 1
                
            return left, right
        
        S = list(S)
        left = 0
        right = len(S)-1
        
        while left < right:
            left, right = getNextPair(left, right, S)
            if left >= right:
                break
            else:
                swap(left, right, S)
                left += 1
                right -= 1
            
        return ''.join(S)

            