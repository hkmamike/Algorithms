class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        # write your code here
        
        charMap = {}
        
        for char in s:
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1
        
        if len(s) % 2 == 0:
            oddQuota = 0
        else:
            oddQuota = 1
        
        for key in charMap:
            if oddQuota <= 0 and charMap[key] % 2 != 0:
                return False
            elif charMap[key] % 2 != 0:
                oddQuota -= 1
                
        return True