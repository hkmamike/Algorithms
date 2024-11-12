class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)

        result = set()
        for n in nums2:
            if n in set1:
                result.add(n)
        return list(result)