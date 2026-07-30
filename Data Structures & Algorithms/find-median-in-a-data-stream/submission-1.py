class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)
        self.data.sort()
    def findMedian(self) -> float:
        n = len(self.data)
        median = self.data[n//2]
        print(n, self.data)
        if n % 2 == 0:
            mid = n//2
            median = (self.data[mid] + self.data[mid-1]) / 2
        return median
         
            
