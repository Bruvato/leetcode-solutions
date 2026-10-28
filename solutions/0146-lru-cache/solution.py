class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hm = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        
        node = self.hm[key]
        self.remove(node)
        self.insert(node)

        return node.val


    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key not in self.hm:
            self.hm[key] = node
            self.insert(node)
        else:
            node = self.hm[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        
        if len(self.hm) > self.cap:
            oldest = self.tail.prev
            self.remove(oldest)

            del self.hm[oldest.key]
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        latest = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = latest
        latest.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
