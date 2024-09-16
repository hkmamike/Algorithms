# proper way
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = head
        fast = head
        # find mid point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd half
        nextN, prev = None, None
        while slow:
            nextN = slow.next
            slow.next = prev
            prev = slow
            slow = nextN
        
        maxVal = 0
        while prev:
            maxVal = max(maxVal, head.val + prev.val)
            prev = prev.next
            head = head.next
        
        return maxVal


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