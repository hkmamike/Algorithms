class Solution:
    def helper(self, num):
        digits = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teenString = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tenString = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        result = ""
        if num > 99:
            result += digits[num // 100] + " Hundred "
            num %= 100
        
        if num < 20 and num > 9:
            result += teenString[num - 10] + " "
        else:
            if num >= 20:
                result += tenString[num // 10] + " "
                num %= 10
            if num > 0:
                result += digits[num] + " "
        return result

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        units = ["Thousand", "Million", "Billion"]

        result = self.helper(num % 1000)
        num = num // 1000

        for u in units:
            if num > 0 and num % 1000 > 0:
                result = self.helper(num % 1000) + u + " " + result
            num = num // 1000

        return result.strip()