class MinStack:

    def __init__(self):
        self.s = []

    def push(self, value: int) -> None:
        if not self.s:
            self.s.append((value, value))
            return

        _, minVal = self.s[-1]
        self.s.append((value, min(value, minVal)))

    def pop(self) -> None:
        return self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


'''
2 0 3 5 1

(2, 2) (0, 0) (3, 0) 

'''
