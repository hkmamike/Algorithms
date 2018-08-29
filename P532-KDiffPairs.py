class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        elif k == 0:
            numMap = {}
            for num in nums:
                if num in numMap:
                    numMap[num] += 1
                else:
                    numMap[num] = 1
            
            count = 0
            for key in numMap:
                if numMap[key] >= 2:
                    count += 1
            return count
        else:
            numsSet = set(nums)
            resultsSet = set()

            for num in nums:
                numPlus = num + k
                numMinus = num - k

                if numPlus in numsSet:
                    entry = sorted([num, numPlus])
                    hashable = tuple(entry)
                    resultsSet.add(hashable)
                if numMinus in numsSet:
                    entry = sorted([num, numMinus])
                    hashable = tuple(entry)
                    resultsSet.add(hashable)

            return len(resultsSet)
        