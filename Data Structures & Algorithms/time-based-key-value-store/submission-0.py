class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.d.get(key):
            self.d[key] = [(value, timestamp)]
        else:
            self.d[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.d.get(key):
            return ""
        else:
            i = 0
            res = ""
            n = len(self.d[key])
            while i < n and timestamp >= self.d[key][i][1]:
                res = self.d[key][i][0]
                i+=1
            return res
