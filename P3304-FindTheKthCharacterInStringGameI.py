class Solution:
    def kthCharacter(self, k: int) -> str:
        def transform(c):
            cOrder = ord(c) - ord("a") + 1
            cOrder = (cOrder) % 26
            return chr(cOrder + ord("a"))
        
        string = "a"
        while len(string) < k:
            string = string + "".join([transform(c) for c in string])
        return string[k-1]