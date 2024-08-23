class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplets.sort()
        t0, t1, t2 = target
        r0, r1, r2 = 0, 0, 0

        for x, y, z in triplets:
            if x <= t0 and y <= t1 and z <= t2:
                r0 = max(r0, x)
                r1 = max(r1, y)
                r2 = max(r2, z)

        return [r0, r1, r2] == target