class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
        nSet = set()
        result = []
        for n in nums:
            if n in nSet:
                result.append(n)
            else:
                nSet.add(n)
        return result
