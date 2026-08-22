# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        cur = slow.next
        prev = slow.next = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        ans, res= head, prev
        while res:
            a,b = ans.next, res.next
            ans.next = res
            res.next = a
            ans, res = a, b


