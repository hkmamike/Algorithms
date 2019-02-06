# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        
        self.nodesMap = {}
        self.nodesMap[head] = RandomListNode(head.label)
        self.stack = [head]
        
        while self.stack:
            item = self.stack.pop()
            itemNext = item.next
            itemRandom = item.random
            
            if itemNext:
                if itemNext not in self.nodesMap:
                    self.nodesMap[itemNext] = RandomListNode(itemNext.label)
                    self.stack.append(itemNext)
                self.nodesMap[item].next = self.nodesMap[itemNext]
            
            if itemRandom:
                if itemRandom not in self.nodesMap:
                    self.nodesMap[itemRandom] = RandomListNode(itemRandom.label)
                    self.stack.append(itemRandom)
                self.nodesMap[item].random = self.nodesMap[itemRandom]
                
        return self.nodesMap[head]
        
        