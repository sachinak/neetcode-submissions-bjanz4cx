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

       
        curr = slow.next
        prev = slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
       
        i = 1

        ans = head
        res = prev
        
        while res:
            t1, t2 = ans.next, res.next
            ans.next = res
            res.next = t1
            ans, res = t1, t2
        
        