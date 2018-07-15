class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        mirror = {'1':'1', '6':'9', '9':'6', '8':'8', '0':'0'}
        num = str(num)
        l = 0
        r = len(num)-1
        
        while l < len(num):
            
            if num[l] not in mirror or num[l] != mirror[num[r]]:
                return False

            l += 1
            r -= 1
            
        return True