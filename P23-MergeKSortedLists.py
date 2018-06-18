# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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