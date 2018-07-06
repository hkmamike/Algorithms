class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        N = len(nums)
        results = []
        
        for key in counter:
            if counter[key] > N/3:
                results.append(key)
                
        return results