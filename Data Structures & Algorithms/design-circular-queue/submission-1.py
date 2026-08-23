class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.cur = 0
        self.front = self.rear = None

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            if not self.front:
                temp = ListNode(value)
                self.front = temp
                self.rear = temp
                self.front.next = self.rear
                self.rear.next = self.front
            else:
                temp = ListNode(value)
                self.rear.next = temp
                self.rear = temp
                self.rear.next = self.front
            self.cur+=1
            return True
        return False


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.cur == 1:
            self.front = None
            self.rear = None
            self.cur-=1
            return True
        self.front = self.front.next
        self.rear.next = self.front
        self.cur -=1
        return True

    def Front(self) -> int:
        if self.front:
            return self.front.val
        return -1

    def Rear(self) -> int:
        if self.rear:
            return self.rear.val
        return -1

    def isEmpty(self) -> bool:
        if self.cur == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.cur == self.cap:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()