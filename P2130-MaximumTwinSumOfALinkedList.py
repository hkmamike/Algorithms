# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        self.d = deque()
        while head:
            self.d.append(head.val)
            head = head.next

        maxPair = 0
        while len(self.d) > 0:
            left = self.d.popleft()
            right = self.d.pop()
            maxPair = max(maxPair, left + right)
        
        return maxPair