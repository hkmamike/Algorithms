class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        sortedDeck = sorted(deck)
        result = collections.deque([])
        
        while len(sortedDeck) > 0:
            insertEntry = sortedDeck.pop()
            result.appendleft(insertEntry)
            
            moveEntry = result.pop()
            result.appendleft(moveEntry)
            
        moveEntry = result.popleft()
        result.append(moveEntry)
            
        return list(result)
        
        