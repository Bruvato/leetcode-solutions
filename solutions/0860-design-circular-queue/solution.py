class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.dummy = Node(-1)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.len = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        node = Node(value)

        rear = self.dummy.prev

        self.dummy.prev = node
        node.next = self.dummy

        node.prev = rear
        rear.next = node

        self.len += 1
        return True

        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        front = self.dummy.next.next

        self.dummy.next = front
        front.prev = self.dummy

        self.len -= 1
        return True
        

    def Front(self) -> int:
        return self.dummy.next.val

    def Rear(self) -> int:
        return self.dummy.prev.val
        

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

'''
3 9 5 0
'''
