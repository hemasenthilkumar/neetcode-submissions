class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev, self.nxt = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.lfu, self.mru = Node(0,0), Node(0,0)
        self.lfu.nxt, self.mru.prev = self.mru, self.lfu

    def insert(self, node):
        # always insert at right
        prev, nxt = self.mru.prev, self.mru
        prev.nxt = nxt.prev = node
        node.nxt,node.prev = nxt, prev
        
    
    def remove(self, node):
        # always remove from left
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newnode = Node(key, value)
        self.cache[key] = newnode
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            to_remove = self.lfu.nxt
            self.remove(to_remove)
            del self.cache[to_remove.key]

