class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        # write your code here
        results = []
        
        for i in range(len(s)-1):
            testString = s[i:i+2]
            
            if testString == '++':
                results.append(s[:i] + '--' + s[i+2:])
                
        return results