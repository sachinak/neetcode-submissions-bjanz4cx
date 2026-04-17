# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        if not h1 and not h2:
            return h1
        
        temp = ListNode()
        res = temp
        while h1 and h2:
            if h1.val < h2.val:
                res.val = h1.val
                h1 = h1.next
            else:
                res.val = h2.val
                h2 = h2.next
            res.next = ListNode()
            res = res.next

        
        while h1:
            res.val = h1.val
            h1 = h1.next
            if h1:
                res.next = ListNode()
                res = res.next
                
        while h2:
            res.val = h2.val
            h2 = h2.next
            if h2:
                res.next = ListNode()
                res = res.next
                
            
        return temp