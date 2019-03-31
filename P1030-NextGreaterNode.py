# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        
        result = []
        unprocessed = []
        i = 0
        
        while head:
            while len(unprocessed) > 0 and head.val > unprocessed[-1][0]:
                index = unprocessed.pop()[1]
                result[index] = head.val
            
            unprocessed.append((head.val, i))
            result.append(-1)
            i += 1
            head = head.next
    
        while len(unprocessed) > 0:
            index = unprocessed.pop()[1]
            result[index] = 0
        return result
    