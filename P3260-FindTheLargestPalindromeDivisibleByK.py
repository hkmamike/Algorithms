class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:

        if k == 1 or k == 3 or k == 9:
            return "9" * n
        if k == 2:
            if n <= 2:
                return "8" * n
            else:
                return "8" + "9" * (n-2) + "8"
        if k == 4:
            if n <= 4:
                return "8" * n
            else:
                return "88" + "9" * (n-4) + "88"
        if k == 5:
            if n <= 2:
                return "5" * n
            else:
                return "5" + "9" * (n-2) + "5"
        if k == 6:
            if n <= 2:
                return "6" * n
            elif n % 2 == 1:
                l = n // 2 - 1
                return "8" + "9" * l + "8" + "9" * l + "8"
            else:
                l = n // 2 - 2
                return "8" + "9" * l + "77" + "9" * l + "8"
        if k == 7:
            if n <= 2:
                return "7" * n
            elif n % 2 == 0:
            # case for 7 when n is even
                result = ["9"] * n
                mid1 = n // 2 - 1
                mid2 = n // 2
                for i in range(9, -1, -1):
                    result[mid1] = result[mid2] = str(i)
                    remainder = 0
                    for j in range(0, n):
                        remainder = (remainder * 10 + ord(result[j]) - ord("0")) % 7
                    if remainder == 0:
                        return "".join(result)
            else:
            # case for 7 when n is odd
                result = ["9"] * n
                mid = n // 2
                for i in range(9, -1, -1):
                    result[mid] = str(i)
                    remainder = 0
                    for j in range(0, n):
                        remainder = (remainder * 10 + ord(result[j]) - ord("0")) % 7
                    if remainder == 0:
                        return "".join(result)
        if k == 8:
            if n <= 6:
                return "8" * n
            else:
                return "888" + "9" * (n-6) + "888"