# coding=utf-8
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n=len(matrix)-1
        m=len(matrix[0])-1
        return self.help(matrix, 0, n, 0, m, target)
        
        
    def help(self, matrix, rowS, rowE, colS, colE, target):
        if rowS>rowE or colS>colE:
            return False
        rowM=(rowS+rowE)/2
        colM=(colS+colE)/2
        if matrix[rowM][colM] ==target:
            return True
        elif matrix[rowM][colM] <target:
            return self.help(matrix, rowM+1, rowE, colS, colM, target) or self.help(matrix, rowM+1, rowE, colM+1 , colE, target) or self.help(matrix, rowS, rowM, colM+1, colE, target)
        else:
            return self.help(matrix, rowS, rowM-1, colS, colM-1, target) or self.help(matrix, rowM, rowE, colS, 
