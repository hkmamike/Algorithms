# general solution for budget more than 1
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True
        def recurse(s, L, R, budget):
            if L >= R:
                return True
            elif s[L] == s[R]:
                return recurse(s, L+1, R-1, budget)
            elif budget == 0:
                return False
            else:
                return any([recurse(s, L, R-1, budget-1), recurse(s, L+1, R, budget-1)])
        return recurse(s, 0, len(s)-1, 1)

# optimal solution
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            
            left, right = left + 1, right - 1
            
        return True
        
        