# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def merge(self, node1, node2):
        if not node1:
            return node2
        elif not node2:
            return node1
        elif node1.val < node2.val:
            node1.next = self.merge(node1.next, node2)
            return node1
        else:
            node2.next = self.merge(node1, node2.next)
            return node2
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        pre, slow, fast = head, head, head
        slow = slow.next
        fast = fast.next.next
        
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
            
        pre.next = None
        
        h1 = self.sortList(head)
        h2 = self.sortList(slow)
        
        return self.merge(h1,h2)