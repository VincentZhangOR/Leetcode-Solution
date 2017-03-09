# coding=utf-8
class Solution(object):
    def uniquePathsWithObstacles (self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]==1:
            return 0
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        flag=0
        special=obstacleGrid[0][0]
        for i in xrange(0,n):
            
            if obstacleGrid[0][i]==1 :
                flag=1
                obstacleGrid[0][i]=0
            else:
                if flag==0:
                                      obstacleGrid[0][i] =1
                if flag==1:
                                      obstacleGrid[0][i] =0
            
        flag=0
        obstacleGrid[0][0]=special
        for i in xrange(0,m):
            if obstacleGrid[i][0]==1 :
                flag=1
                obstacleGrid[i][0]=0
            elif flag==0:
                obstacleGrid[i][0]=1
            else:
                obstacleGrid[i][0]=0
              
        for i in xrange(1,m):
            for j in xrange(1,n):
                    if obstacleGrid[i][j] ==1:
                        #flag=1
                                          obstacleGrid[i][j] =0
                    else:
                                          obstacleGrid[i][j] =obstacleGrid[i
