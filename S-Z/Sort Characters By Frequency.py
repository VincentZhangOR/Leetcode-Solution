# coding=utf-8
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for x in s:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        h = []
        
        for x in d:
            heapq.heappush(h,(-d[x],x ))
        #print h,d
        res = ''
        for x in d:
            num, a = heapq.heappop(h)
            res += a * (-num) 
        return res
