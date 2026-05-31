class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in  self.store:
             self.store[key] = {}
        
        self.store[key][timestamp] = value


    def get(self, key: str, timestamp: int) -> str:
        if key not in  self.store:
            return ""
        
        while timestamp >= 0:
            if timestamp not in  self.store[key]:
                timestamp -= 1
            else:
                return  self.store[key][timestamp]
            
        return ""
        
