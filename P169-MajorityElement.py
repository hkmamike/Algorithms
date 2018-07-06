class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter(nums)
        return counter.most_common(1)[0][0]