class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        counter = collections.Counter(words)
        h = []
        
        for entry in counter:
            heapq.heappush(h, [-counter[entry], entry])
            
        res = []
        while len(res) < k and len(h) > 0:
            word = heapq.heappop(h)
            res.append(word[1])
            
        return res
        
            