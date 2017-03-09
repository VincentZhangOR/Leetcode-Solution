# coding=utf-8
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        return self.C(range(1,n+1), k)
         
    def C(self, List, k):
        res = []
        length = len(List)
        if k <= 0 or length < k:
            return res
        for i in xrange(length):
            if k == 1:
                res.append( list ((List[i],)) )
            else:
                for item in self.C (List[i+1:], k-1):
                    res.append( [List[i]] + item )
        return res
            
        
