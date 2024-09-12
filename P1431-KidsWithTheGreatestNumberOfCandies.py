class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxC = max(candies)

        result = []
        for c in candies:
            if c + extraCandies >= maxC:
                result.append(True)
            else:
                result.append(False)
        
        return result
