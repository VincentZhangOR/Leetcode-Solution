# coding=utf-8
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        for x in matrix:
            x.insert(0,float('-inf' ))
            x.append(float('-inf'))
        m = len(matrix[0])
        matrix = [[float('-inf')]*m] + matrix + [[float(' -inf')]*m]
        n = len(matrix)
        d = collections.defaultdict (int)
        ret = 1
        
        def dfs(used, i, j, res):
            if (i,j) in d:
                return d[i,j]
            if ((i-1,j) in used and (i+1,j) in used and (i,j-1) in used and (i,j+1) in used) or (matrix[i-1][j] <=matrix[i][j] and matrix[i+1][j] <=matrix[i][j] and matrix[i][j-1] <=matrix[i][j] and matrix[i][j+1] <=matrix[i][j]):
                return res
            temp = res
            if (i-1,j) not in used and matrix[i-1][j] >matrix[i][j]:
                used.add((i-1,j))
                res = max(res, dfs (used, i-1, j, temp)+1)
                used.remove((i-1,j))
            if (i+1,j) not in used and matrix[i+1][j] >matrix[i][j]:
                used.add((i+1,j))
                res = max(res, dfs (used, i+1, j, temp)+1)
                used.remove((i+1,j))
            if (i,j-1) not in used and matrix[i][j-1] >matrix[i][j]:
                used.add((i,j-1))
                res = max(res, dfs (used, i, j-1, temp)+1)
                used.remove((i,j-1))
            if (i,j+1) not in used and matrix[i][j+1] >matrix[i][j]:
                used.add((i,j+1))
                res = max(res, dfs (used, i, j+1, temp)+1)
                used.remove((i,j+1))
            d[i,j] = res

