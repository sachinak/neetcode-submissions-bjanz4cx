# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        l = 0
        while cur:
            l+=1
            cur=cur.next
        if l - n == 0:
            return head.next
        if l == 1 and n == 1:
            return None
        cur = head
        nxt = cur.next
        i = 0
        while cur:
            if i == l - n - 1:
                cur.next = nxt.next
                break
            i+=1
            cur = cur.next
            nxt = nxt.next
        return head