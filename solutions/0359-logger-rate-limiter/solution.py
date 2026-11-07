class Logger:

    def __init__(self):
        self.old = {}
        self.new = {}
        self.t = 0
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if timestamp >= self.t + 20:
            self.old.clear()
            self.new.clear()
            self.t = timestamp
            
        elif timestamp >= self.t + 10:
            self.old = self.new
            self.new = {}
            self.t = timestamp

        if message in self.new:
            return False
        if message in self.old and timestamp < self.old[message] + 10:
            return False
        
        self.new[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
