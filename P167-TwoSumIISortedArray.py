class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def binarySearch(neededNum, numbers, startIdx):
            L = startIdx + 1
            R = len(numbers) - 1

            while L < R:
                M = (L + R) // 2
                if numbers[M] < neededNum:
                    L = M + 1
                else:
                    R = M
            return L

        for i, n in enumerate(numbers):
            neededNum = target - n
            bestIdx = binarySearch(neededNum, numbers, i)
            if numbers[bestIdx] == neededNum:
                return [i+1, bestIdx+1]

        return False