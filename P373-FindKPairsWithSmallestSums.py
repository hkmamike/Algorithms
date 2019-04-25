class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        if not nums1 or not nums2:
            return []
        
        res = []
        h = [[nums1[0]+nums2[0], 0, 0]]
        used = set((0,0))
        
        while len(res) < k and len(h) > 0:
            pair = heapq.heappop(h)
            res.append([nums1[pair[1]], nums2[pair[2]]])
            
            if pair[1] + 1 < len(nums1) and (pair[1]+1, pair[2]) not in used:
                used.add((pair[1]+1, pair[2]))
                heapq.heappush(h, [nums1[pair[1]+1] + nums2[pair[2]], pair[1]+1, pair[2]])
            
            if pair[2] + 1 < len(nums2) and (pair[1], pair[2]+1) not in used:
                used.add((pair[1], pair[2]+1))
                heapq.heappush(h, [nums1[pair[1]] + nums2[pair[2]+1], pair[1], pair[2]+1])
                
        return res
            