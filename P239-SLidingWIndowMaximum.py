



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
        