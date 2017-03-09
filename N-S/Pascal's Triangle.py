# coding=utf-8
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        res=[[1],[1,1]]
        pre=[1,1]
        for i in xrange(numRows-2):
            mid=[]
            for j in xrange(len(pre)-1 ):
                mid.append(pre[j] +pre[j+1])
            mid=[1]+mid+[1]
            res.append(mid)
            pre=mid
        return res
