# coding=utf-8
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in -place instead.
        """
        s1=[]
        s2=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j]==0:
                    if i not in s1:
                        s1.append(i)
                    if j not in s2:
                        s2.append(j)
        for x in s1:
            matrix[x]=[0]*n
        for i in xrange(m):

            for y in s2:

                matrix[i][y]=0
                
        
        
