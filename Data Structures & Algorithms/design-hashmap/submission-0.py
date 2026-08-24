class MyHashMap:

    def __init__(self):
        self.arr = []

    def put(self, key: int, value: int) -> None:
        
        for idx, ele in enumerate(self.arr):
            k, v = ele
            if k == key:
                self.arr[idx] = [key, value]
                return
        self.arr.append([key, value])

    def get(self, key: int) -> int:
        for idx, ele in enumerate(self.arr):
            k, v = ele
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        flag = False
        for idx, ele in enumerate(self.arr):
            k, v = ele
            if k == key:
                flag = True
                break
        if not flag:
            return
        del self.arr[idx]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)