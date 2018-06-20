class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        
        origin = prefix = ListNode(0)
        origin.next = head
        
        for _ in range(m-1):
            prefix = prefix.next
            
        reverse = None
        current = prefix.next
        
        for _ in range(n-m+1):
            nextNode = current.next
            current.next = reverse
            reverse = current
            current = nextNode
            
        prefix.next.next = current
        prefix.next = reverse
        
        return origin.next