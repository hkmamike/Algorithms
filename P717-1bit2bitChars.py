class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if not bits or bits == [0]:
            return True
        
        i = 0
        while i <= len(bits) - 2:
            if bits[i] == 0:
                i += 1
            elif bits[i] == 1:
                i += 2
        
        if i == len(bits) - 1:
            return True
        else:
            return False