class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        def newPair():
            return [len(s)-1, 0]

        charSet = defaultdict(newPair)
        for i, c in enumerate(s):
            charSet[c][0] = min(charSet[c][0], i)
            charSet[c][1] = max(charSet[c][1], i)
            
        result = []
        started = set()
        currentSegment = 0
        for i, c in enumerate(s):
            if charSet[c][0] == i:
                started.add(c)
            if charSet[c][1] == i:
                started.remove(c)

            currentSegment += 1
            if len(started) == 0:
                result.append(currentSegment)
                currentSegment = 0

        return result