# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        res = head
        cnt = 0
        while res:
            res = res.next
            cnt+=1
        
        dummy = ListNode(0, head)
        prev = dummy
        
        for i in range(cnt//k):
            cur = prev.next
            for _ in range(k-1):
                nxt = cur.next
                cur.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
            prev = cur
        return dummy.next