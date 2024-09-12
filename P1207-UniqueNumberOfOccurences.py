class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        C = Counter(arr)
        occurenceSet = set()

        for k, v in C.items():
            if v in occurenceSet:
                return False
            else:
                occurenceSet.add(v)
        return True
