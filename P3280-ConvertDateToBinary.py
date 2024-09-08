class Solution:
    def convertDateToBinary(self, date: str) -> str:
        
        y, m, d = date.split("-")

        def stringBinary(s):
            return str(bin(int(s)))[2:]

        return stringBinary(y) + "-" + stringBinary(m) + "-" + stringBinary(d)