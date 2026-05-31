class LRUCache:

    def __init__(self, capacity: int):
        self.recently_used = list()
        self.tracker = dict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:

        if key in self.tracker:
            self.recently_used.remove(key)
            self.recently_used.append(key)
            if len(self.recently_used) > self.capacity:
                self.recently_used.pop(0)
            return self.tracker[key]
        
        return -1
        

    def put(self, key: int, value: int) -> None:

        self.tracker[key] = value

        if key in self.recently_used:
            self.recently_used.remove(key)
            self.recently_used.append(key)
        else:
            self.recently_used.append(key)
        
        if len(self.recently_used) > self.capacity:
                removed = self.recently_used.pop(0)
                del self.tracker[removed]


        
