# coding=utf-8
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        res=grid
        for i in xrange(1,n):
            res[0][i]+=res[0][i-1]
        for j in xrange(1,m):
            res[j][0]+=res[j-1][0]
        for i in xrange(1,m):
            for j in xrange(1,n):
                res[i][j]+=min(res[i -1][j],res[i][j-1])
        return res[m-1][n-1]
