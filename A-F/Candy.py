# coding=utf-8
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        d = [1 for x in xrange(n)]
        for i in xrange(n-1):
            if ratings[i+1] > ratings[i]:
                d[i+1] = d[i] + 1
        #print d
        for i in xrange(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                d[i-1] = max(d[i] + 1, d[i-1])
        res = 0
        for x in d:
            res += x
        #print d
        return res
