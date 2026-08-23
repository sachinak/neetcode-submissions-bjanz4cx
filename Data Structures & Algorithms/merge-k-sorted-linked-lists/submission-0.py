# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        if not lists:
            return 
        for l in lists:
            while l:
                heapq.heappush(q, l.val)
                l = l.next
        if not q:
            return
        head = ListNode()
        cur = head

        while q:
            v = heapq.heappop(q)
            cur.val = v
            if len(q) > 0:
                cur.next = ListNode()
            cur = cur.next
        
        
        return head