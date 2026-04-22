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
        nh = Node(0)
        if not head:
            return None
        sh = nh
        second = head
        d = {}
        while second:
            sh.val = second.val
            sh.random = None
            if second.next:
                temp = Node(second.next.val)
                sh.next = temp
            d[second] = sh
            sh = sh.next
            second = second.next
        second = head
        sh = nh
        while second:
            
            if second.random:
                temp = d[second.random]
                sh.random = temp
            second = second.next
            sh = sh.next
             
        return nh