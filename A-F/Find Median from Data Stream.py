# coding=utf-8
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.n = 0
        self.max_h = []
        self.min_h = []
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if self.n == 0:
            self.max_h.append(-num)
        #elif self.n == 1:
        #    self.max_h = [min()]
        elif self.n % 2 == 0:
            if num <= self.min_h[0]:
                heapq.heappush(self .max_h, -num)
            else:
                heapq.heappush(self .min_h, num)
                heapq.heappush(self .max_h, -(heapq .heappop(self.min_h )))
        else:
            if num < -self.max_h[0]:
                heapq.heappush(self .max_h, -num)
                heapq.heappush(self .min_h, -(heapq .heappop(self.max_h )))
            else:
                heapq.heappush(self .min_h, num)
        self.n += 1
        
        
    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.n == 0:
            return 0.0
        if self.n % 2 == 0:
            return (-self.max_h[0] + self.min_h[0]) / 2.0
        else:
            return float(-self .max_h[0])
        

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
