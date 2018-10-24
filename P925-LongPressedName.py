class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        index = 0
        
        for n in name:
            while index < len(typed):
                if typed[index] != n:
                    index += 1
                else:
                    break
            
            if index >= len(typed):
                return False
            else:
                index += 1
            
        return True
            
                    