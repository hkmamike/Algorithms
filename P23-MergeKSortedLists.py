# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Optimal Solution
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        origin = head = ListNode(None)
        h = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, i, node))
        
        while h:
            nodeVal, idx, node = heappop(h)
            head.next = node
            node = node.next
            head = head.next
            if node:
                heapq.heappush(h, (node.val, idx, node))
        
        return origin.next

from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists):

        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        
        for i,node in enumerate(lists):
            if node: q.put((node.val, i, node))
                
        while q.qsize()>0:
            smallest = q.get()
            curr.next = smallest[2]
            curr_id = smallest[1]
            curr=curr.next
            if curr.next: q.put((curr.next.val, curr_id, curr.next))
                
        return dummy.next