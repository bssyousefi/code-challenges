class TimeMap:

    def __init__(self):
        self.values = {}
        self.times = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.times:
            self.times[key].append(timestamp)
            self.values[key].append(value)
            return # This return and 2 lines above are only for the situation in which
            # setting is done in a time increasing order
            i = self.find(key, timestamp)
            if i < len(self.times[key]) and self.times[key][i] == timestamp:
                self.values[key][i] = value
            else:
                self.times[key] = [*self.times[key][0:i], timestamp, *self.times[key][i:]]
                self.values[key] = [*self.values[key][0:i], value, *self.values[key][i:]]
        else:
            self.values[key] = [value]
            self.times[key] = [timestamp]
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.times:
            i = self.find(key, timestamp)
            if i < len(self.times[key]) and self.times[key][i] == timestamp:
                return self.values[key][i]
            else:
                if i == 0:
                    return ""
                else:
                    return self.values[key][i-1]
        else:
            return ""
        
    def find(self, key: str, timestamp: int) -> int:
        l = 0
        r = len(self.times[key]) - 1

        if self.times[key][r] < timestamp:
            return r+1
        elif self.times[key][r] == timestamp:
            return r

        while(l<=r):
            m = (l+r) // 2
            if self.times[key][m] == timestamp:
                return m
            elif self.times[key][m] < timestamp:
                l = m + 1
            else:
                r = m - 1
        return l

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
