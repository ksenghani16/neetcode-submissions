class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache=collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value=self.cache.pop(key)
        self.cache[key]=value
        return value
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        if len(self.cache)>=self.capacity:
            evicted_value,evicted_item=self.cache.popitem(last=False)
        self.cache[key]=value
        
