# coding=utf-8
class Solution(object):
    def findDiagonalOrder(self, matrix ):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        res = []
        i = 0
        j = 0
        flag = 1
        while True:
            if i == m-1 and j == n-1:
                res.append (matrix[i][j])
                break
            res.append(matrix[i][j])
            if flag == 0:
                i += 1
                j -= 1
                if i > m-1 and j < 0:
                    i = m-1
                    j = 1
                    flag = 1
                elif i > m-1:
                    i = m-1
                    j += 2
                    flag = 1
                elif j < 0:
                    j = 0
                    flag = 1
            else:
                i -= 1
                j += 1
                if i < 0 and j > n-1:
                    i = 1
                    j = n-1
                    flag = 0
                elif i < 0:
                    i = 0
                    flag = 0
                elif j > n-1:
                    j = n-1
                    i += 2
                    flag = 0
            #print i,j
        return res
