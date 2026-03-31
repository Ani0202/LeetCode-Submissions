class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        largest_in_small = -heapq.heappop(self.left)
        heapq.heappush(self.right, largest_in_small)
        if len(self.left) < len(self.right):
            smallest_in_right = heapq.heappop(self.right)
            heapq.heappush(self.left, -smallest_in_right)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (self.right[0] - self.left[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
