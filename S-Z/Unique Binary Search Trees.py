# coding=utf-8
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        record=[0]*(n+1)
        record[0]=1
        record[1]=1
        for i in xrange(2,n+1):
            record[i]=record[i-1]
            for j in xrange(1,i):
                record[i]+=record[i-j -1]*record[j]
        return record[n]
        
            
