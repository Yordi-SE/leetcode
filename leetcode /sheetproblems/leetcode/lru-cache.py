class Node:
    def __init__(self,key,val,next,prev):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node(None, None, None, None)
        self.tail = self.head

    def get(self, key: int) -> int:

        if key in self.hashmap:

            val = self.hashmap[key].val

            self.removeNode(key)
            self.addNode(self.hashmap[key])

            return val
        
        else:
            return -1


    def put(self, key: int, value: int) -> None:

        if key in self.hashmap:
            self.hashmap[key].val = value
            self.removeNode(key)
            
            self.addNode(self.hashmap[key])
        else:
            self.hashmap[key] = Node(key,value,None,None)
            self.addNode(self.hashmap[key])
        
        if self.capacity < len(self.hashmap):
            key = self.head.next.key
            
            self.removeNode(self.head.next.key)
            del self.hashmap[key]
    def removeNode(self,key):
        if self.hashmap[key] == self.tail:
            return
        self.hashmap[key].prev.next = self.hashmap[key].next
        self.hashmap[key].next.prev = self.hashmap[key].prev
        
    
    def addNode(self,node):
        if node == self.tail:
            return
        node.prev = self.tail
        self.tail.next = node
        node.next = None
        self.tail = node
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)