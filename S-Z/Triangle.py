# coding=utf-8
class Solution(object):
    def minimumTotal(self, triangle ):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n=len(triangle)
        if n==0:
            return 0
        res=[[] for i in xrange(n)]
        res[0].append(triangle[0][0] )
        for i in xrange(1,n):
            for j in xrange(len (triangle[i])):
                if j==0:
                    res[i].append (res[i-1][j] +triangle[i][j])
                elif j<len (triangle[i])-1:
                    res[i].append (min(res[i-1][j-1] ,res[i-1][j] )+triangle[i][j])
                else:
                    res[i].append (res[i-1][j-1] +triangle[i][j])
            #print res
        ans=res[-1][0]

