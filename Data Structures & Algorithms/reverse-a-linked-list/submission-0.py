# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        if head == None:
            return head

        while head:
            l.append(head.val)
            head = head.next

        temp = ListNode()
        ans = temp
        n = len(l)
        for i,v in enumerate(l[::-1]):
            temp.val = v
            if i == n-1:
                break
            temp.next = ListNode()
            temp = temp.next

            
        return ans