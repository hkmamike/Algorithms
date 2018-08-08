# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head.next:
            return head
        
        number = 1
        origin = head
        
        while head.next:
            number += 1
            head = head.next
            
        middle = number // 2 + 1
        
        for _ in range(middle-1):
            origin = origin.next
            
        return origin