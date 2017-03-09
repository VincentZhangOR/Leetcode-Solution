# coding=utf-8
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        h = [1]
        d = set()
        ans = 0
        while n > 0:
            n -= 1
            ans = heapq.heappop(h)
            if 2*ans not in d:
                heapq.heappush(h,2*ans )
                d.add(2*ans)
            if 3*ans not in d:
                heapq.heappush(h,3*ans )
                d.add(3*ans)
            if 5*ans not in d:
                heapq.heappush(h,5*ans )
                d.add(5*ans)
        return ans
