# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next
        if not fast:
            return False
        
        while slow and fast:
            if slow == fast:
                return True
            slow = slow.next

            if not fast.next:
                return False
            fast = fast.next.next

        return slow == fast