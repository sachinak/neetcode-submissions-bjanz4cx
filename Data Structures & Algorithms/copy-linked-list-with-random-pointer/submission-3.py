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
            return 
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
        sh = nh
        second = head

        while second:
            if second.random:
                sh.random = d[second.random]
            sh = sh.next
            second = second.next
        return nh