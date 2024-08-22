

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        result = []
        
        for i, num in enumerate(nums):
            while d and nums[d[-1]] < num:
                d.pop()
            if d and i - d[0] >= k:
                d.popleft()
            d.append(i)
            result.append(nums[d[0]])

        return result[k-1:]
         
        

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        window = deque(nums[:k])
        maxV = max(nums[:k])
        result = [maxV]

        idx = k
        while idx < len(nums):
            lastValue = window.popleft()
            window.append(nums[idx])
            if lastValue != maxV:
                maxV = max(maxV, nums[idx])
                result.append(maxV)
            else:
                maxV = max(window)
                result.append(maxV)
            idx += 1
        return result
        