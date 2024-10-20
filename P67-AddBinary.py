class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aReverse = a[::-1]
        bReverse = b[::-1]
        result = []
        carry = 0
        for i in range(max(len(a), len(b))):
            aVal = int(aReverse[i]) if i < len(a) else 0
            bVal = int(bReverse[i]) if i < len(b) else 0
            carry += aVal + bVal
            remainder = carry % 2
            carry = carry // 2
            result.append(str(remainder))
        if carry > 0:
            result.append(str(carry))

        return "".join(result)[::-1]