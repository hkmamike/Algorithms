class Solution:
    """
    @param A: lists A
    @param B: lists B
    @return: the index mapping
    """
    def anagramMappings(self, A, B):
        # Write your code here
        mapB = {}
        
        for i, char in enumerate(B):
            if char in mapB:
                mapB[char].append(i)
            else:
                mapB[char] = [i]
                
        P = []
        
        for char in A:
            P.append(mapB[char][-1])
            
        return P