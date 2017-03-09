# coding=utf-8
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m=len(word1)+1
        n=len(word2)+1
        res=[[0 for i in range(n)] for j in range(m)]
        temp=0
        for j in xrange(n):
            res[0][j]=j
        for i in xrange(m):
            res[i][0]=i
        for i in xrange(1,m):
            for j in xrange(1,n):
                if word1[i-1] ==word2[j-1]:
                    temp=0
                else:
                    temp=1
                res[i][j]=min (res[i][j-1]+1 ,res[i-1][j]+1 ,res[i-1][j-1]
