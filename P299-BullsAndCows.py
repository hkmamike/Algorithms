class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secretHashMap = {}
        
        for char in secret:
            if char in secretHashMap:
                secretHashMap[char] += 1
            else:
                secretHashMap[char] = 1
                
        A = 0
        B = 0
        
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                A += 1
                secretHashMap[guess[i]] -= 1
        
        for i in range(len(guess)):
            if guess[i] != secret[i]:
                if guess[i] in secretHashMap and secretHashMap[guess[i]] > 0:
                    B += 1
                    secretHashMap[guess[i]] -= 1
                
        return str(A) + "A" + str(B) + "B"