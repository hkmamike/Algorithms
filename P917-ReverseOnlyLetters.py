class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        
        left = 0
        right = len(S)-1
        
        while left < right:
            while S[left].isalpha() == False and left < right:
                left += 1
            
            while S[right].isalpha() == False and right > left:
                right -= 1
            
            S[left], S[right] = S[right], S[left]
            left += 1
            right -= 1
        
        return "".join(S)
            