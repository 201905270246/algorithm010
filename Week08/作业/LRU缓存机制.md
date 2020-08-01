```
class LRUCache:
    from collections import OrderedDict
    def __init__(self, capacity:int):
        self.size = capacity
        self.lrucache = OrderedDict()
    
    def get(self, key:int) -> int:
        if key in self.lrucache:
            self.lrucache.move_to_end(key)
        return self.lrucache.get(key, -1)
    
    def put(self, key:int, value:int) -> None:
        if key in self.lrucache:
            del self.lrucache[key]
        self.lrucache[key] = value
        if len(self.lrucache) > self.size:
            self.lrucache.popitem(last = False)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

```
