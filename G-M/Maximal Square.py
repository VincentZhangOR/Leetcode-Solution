# coding=utf-8
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix==None or matrix==[]:
            return 0
        m=len(matrix)
        n=len(matrix[0])
        d=[[0]*n for x in xrange(m)]
        ans=0
        for i in xrange(m):
            for j in xrange(n):
                d[i][j]=int (matrix[i][j])
                if i and j and d[i][j] :
                    d[i][j]=min(d[i -1][j],d[i][j-1] ,d[i-1][j-1])+1
                ans=max(ans,d[i][j])
        return ans*ans
