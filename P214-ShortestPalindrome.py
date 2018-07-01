class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPalindrome(s):
            return s == s[::-1]
        
        n = len(s)
        
        for i in range(n-1, -1, -1):
            if isPalindrome(s[:i+1]):
                return s[i+1:][::-1] + s
            
        return s[1:][::-1] + s
        