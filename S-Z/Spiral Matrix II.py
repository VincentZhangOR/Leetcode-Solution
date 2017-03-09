# coding=utf-8
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==0:
            return []
        res=[[0]*n for i in xrange(n )]
        up=0
        down=n-1
        left=0
        right=n-1
        direct=0
        count=1
        while True:
            if direct==0:
                for i in xrange(left , right+1):
                    res[up][i]=count
                    count+=1
                up+=1
            if direct==1:
                for i in xrange(up, down+1):
                    res[i][right] =count
                    count+=1
                right-=1
            if direct==2:
                for i in xrange (right,left-1,-1):
                    res[down][i] =count
                    count+=1
                down-=1
            if direct==3:
                for i in xrange(down , up-1, -1):
                    res[i][left] =count
                    count+=1
                left+=1
            if left>right or up>down
