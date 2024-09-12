class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        C = Counter(nums)
        operations = 0
        for i, n in enumerate(nums):
            if C[n] == 0:
                continue
            target = k - n
            if target in C:
                if target != n and C[target] > 0:
                    operations += 1
                    C[target] -= 1
                    C[n] -= 1
                elif target == n and C[target] >= 2:
                    operations += 1
                    C[target] -= 2 

        return operations
