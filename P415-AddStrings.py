class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        r1 = num1[::-1]
        r2 = num2[::-1]
        N = max(len(r1), len(r2))

        result = []
        carry = 0
        for i in range(N):
            r1Value = int(r1[i]) if len(r1) > i else 0
            r2Value = int(r2[i]) if len(r2) > i else 0
            carry = carry + r1Value + r2Value
            result.append(carry % 10)
            carry = carry // 10
        
        if carry > 0:
            result.append(carry)
        result = [str(x) for x in result]
        result.reverse()
        return "".join(result)
        