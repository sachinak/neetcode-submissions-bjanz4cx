# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        carry = 0
        while l1 and l2:
            tot = l1.val+l2.val+carry
            
            carry = tot//10
            tmp = ListNode(tot%10)
            cur.next = tmp
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            tot = l1.val+carry
            carry = tot//10
            
            tmp = ListNode(tot%10)
            cur.next = tmp
            cur = cur.next
            l1 = l1.next
        
        while l2:
            tot = l2.val+carry
            carry = tot//10
            
            tmp = ListNode(tot%10)
            cur.next = tmp
            cur = cur.next
            l2 = l2.next
        if carry:
            cur.next = ListNode(carry)
           
        
        return res.next
        
