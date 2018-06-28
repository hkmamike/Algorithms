
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        length = len(s)
        maxS = ""
        
        if len(s) == 0:
            return ""
        elif len(s) == 1:
            return s
        
        for i in range(1,length):
            longest = self.expand(s,i,'even')
            if len(longest) > len(maxS):
                maxS = longest
            
            longest = self.expand(s,i,'odd')
            if len(longest) > len(maxS):
                maxS = longest
        
        return maxS
    
    def expand(self,s,i,mode):
        
        if mode == 'odd':
            l = i
            r = i
            
        elif mode == 'even':
            if i == 0:
                l = i
                r = i+1
            else:
                l = i-1
                r = i
            if s[l] != s[r]:
                return s[i]
        
        while l>=0 and r <= len(s) -1 and s[l] == s[r]:
            l = l-1
            r = r+1
            
        return s[l+1:r]