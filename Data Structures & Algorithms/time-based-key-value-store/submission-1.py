class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key]=[]
        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
       # do a binary search to find lowest nearest value
        if key not in self.time_map:
            return ""
        values=self.time_map[key]
        low = 0
        high = len(values) -1
        target = ""
        while low <= high:
            mid = low + ((high-low)//2)
            if values[mid][1] <= timestamp:
                target = values[mid][0]
                low = mid + 1
            else:
                high = mid - 1
        return target