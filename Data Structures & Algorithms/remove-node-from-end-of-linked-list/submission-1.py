# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ptr = head
        m = 0
        while ptr:
            ptr = ptr.next
            m+=1
        if m == 1 and n == 1:
            return None
        if m - n == 0:
            return head.next
        ptr = head
        i = 0
        f, s = head, head.next
        while s:
            print(i,m,n,f.val,s.val)
            if i == m - n - 1:
                f.next = s.next
                break
            else:
                f = f.next
                s = s.next
            i+=1
        return head
        