class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        S1 = set(nums1)
        S2 = set(nums2)

        return [list(S1-S2), list(S2-S1)]
