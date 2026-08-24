class MyHashSet:

    def __init__(self):
        self.arr = []

    def add(self, key: int) -> None:
        for i, v in enumerate(self.arr):
            if v == key:
                return
        self.arr.append(key)
        

    def remove(self, key: int) -> None:
        flag = False
        for i, v in enumerate(self.arr):
            if v == key:
                flag = True
                break
        if not flag:
            return
        del self.arr[i]
       

    def contains(self, key: int) -> bool:
        
        for i, v in enumerate(self.arr):
            if v == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)