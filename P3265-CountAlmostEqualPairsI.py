class Solution:
    def countPairs(self, nums: List[int]) -> int:
        
        def isAlmostEqual(n1, n2):
            if n1 == n2:
                return True
            n1 = str(n1)
            n2 = str(n2)

            if len(n1) < len(n2):
                n1 = "0" * (len(n2)-len(n1)) + n1
            if len(n2) < len(n1):
                n2 = "0" * (len(n1)-len(n2)) + n2
            if int(n1) == int(n2):
                return True

            for i in range(len(n1)-1):
                for j in range(i+1, len(n1)):
                    swappedN1 = n1[:i] + n1[j] + n1[i+1:j] + n1[i] + n1[j+1:]
                    swappedN1Val = int(swappedN1)
                    if swappedN1Val == int(n2):
                        return True
            return False


        result = 0
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if isAlmostEqual(nums[i], nums[j]):
                    result += 1
        return result