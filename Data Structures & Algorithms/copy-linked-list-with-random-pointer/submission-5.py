"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d={}
        if not head:
            return 
        res = sec = Node(head.val)
        cur = head
        while cur:
            sec.val = cur.val
            sec.random = None
            
            if cur.next:
                tmp = Node(cur.next.val)
                sec.next = tmp
            d[cur] = sec
            sec = sec.next
            cur = cur.next
        
        sec = res
        cur = head
        while cur:
            if cur.random:
                sec.random = d[cur.random]
            cur = cur.next
            sec = sec.next
        return res