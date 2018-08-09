class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        else:
            result = []
        
        def addEntry(start, end, result):
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(end))
            
        start = None
        for i in range(len(nums)):
            if start == None:
                start = nums[i]
            elif nums[i] != nums[i-1] + 1:
                addEntry(start, nums[i-1], result)
                start = nums[i]
                
        addEntry(start, nums[-1], result)
        return result