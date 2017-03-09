# coding=utf-8
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        while matrix!=[]:
            m=len(matrix)
            n=len(matrix[0])
            if m==1:
                for x in matrix[0]:
                    res.append(x)
                break
            if n==1:
                for x in matrix:
                    res.append(x[0])
                break
            for x in matrix[0]:
                res.append(x)
            matrix.remove(matrix[0])

            for x in matrix:
                res.append(x[-1])
                x.remove(x[-1])

            for x in matrix[-1][::-1]:
                res.append(x)
            matrix.remove(matrix[-1])
            for x in matrix[::-1]:
                res.append(x[0])
                x.remove(x[0])
                if x==[]:
                    matrix.remove(x)
        return res
