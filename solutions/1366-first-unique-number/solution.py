class FirstUnique:

    def __init__(self, nums: list[int]):
        self.hm = {}
        self.q = deque(nums)

        for num in nums:
            self.hm[num] = self.hm.get(num, 0) + 1
        
    def showFirstUnique(self) -> int:
        while self.q and self.hm[self.q[0]] != 1:
            self.q.popleft()

        if not self.q:
            return -1
        
        uni = self.q.popleft()
        self.q.appendleft(uni)
        return uni

    def add(self, value: int) -> None:
        self.hm[value] = self.hm.get(value, 0) + 1
        self.q.append(value)



# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
