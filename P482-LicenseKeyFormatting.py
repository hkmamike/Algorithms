class Solution:
    def licenseKeyFormatting(self, S, K):
        
        S = S.upper().replace('-', '')
        result = ""
        index = len(S)-1
        
        while index >= 0:
            
            if index > K-1:
                result = "-" + S[index-K+1:index+1] + result
                index -= K
                
            elif index <= K-1:
                result = S[:index+1] + result
                index = -1
                
        return result