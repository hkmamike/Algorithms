class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        maxSet = 0
        visited = [False] * len(nums)
        
        for i in nums:
            count = 0
            index = i
            
            while not visited[index]:
                visited[index] = True
                index = nums[index]
                count += 1
                
            maxSet = max(maxSet, count)
                
        return maxSet
    