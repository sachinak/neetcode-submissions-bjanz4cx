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
            res = ""
            n = len(self.d[key])
            l = 0
            r = n - 1

            while l <= r:
                m = (l+r)//2

                if self.d[key][m][1] <= timestamp:
                    res = self.d[key][m][0]
                    l = m+1
                else:
                    r = m- 1
            return res
