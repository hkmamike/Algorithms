class Solution:
    def countBits(self, num: int) -> List[int]:
        
        bits = [0] * (num+1)
        
        for i in range(1, num+1):
            bits[i] = bits[i//2]
            if i % 2 == 1:
                bits[i] = bits[i] + 1
            
        return bits