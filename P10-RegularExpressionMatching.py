class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        cache = [[False for _ in range(len(s)+1) ] for _ in range(len(p)+1)]
        
        cache[0][0] = True
        
        for r in range(2, len(p)+1):
            cache[r][0] = cache[r-2][0] and p[r-1] == '*'
            
        for r in range(1, len(p)+1):
            for c in range(1, len(s)+1):
                if p[r-1] != '*':
                    cache[r][c] = cache[r-1][c-1] and (s[c-1] == p[r-1] or p[r-1] == '.')
                
                else:
                    cache[r][c] = cache[r-1][c] or cache[r-2][c]
                    
                    if p[r-2] == s[c-1] or p[r-2] == '.':
                        cache[r][c] = cache[r][c] or cache[r][c-1]
                    
        return cache[-1][-1]