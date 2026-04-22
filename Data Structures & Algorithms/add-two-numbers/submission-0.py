# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        h1= l1
        h2= l2
        s1=""
        s2=""
        while h1:
            s1+=str(h1.val)
            h1=h1.next
        while h2:
            s2+=str(h2.val)
            h2=h2.next
        l3 = ListNode()
        h3 = l3
        res = str(int(s1[::-1]) + int(s2[::-1]))
        for r in res[::-1]:
            t = ListNode(int(r))
            h3.next = t
            h3 = h3.next
        return l3.next