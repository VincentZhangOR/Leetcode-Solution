# coding=utf-8
class Solution(object):
    global res
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n <= 3:
            return [] if n > 1 else [['Q']]
        board = [-1 for x in range(n )]
        res = []
        self.dfs(0, [], res, board, n)
        return res
        
    
    def dfs(self, depth, ans, res, board, n):
        if depth == n:
            res.append(ans+[])
            return
        for i in xrange(n):
            if self.check(depth, i, board):
                board[depth] = i
                ans.append('.' * i + 'Q' + '.' * (n - i - 1))
                (self.dfs(depth + 1, ans, res, board, n ))
                ans.pop()
                board[depth] = -1
            
        
    def check(self, depth, col, board):
        #print depth, board
        for i in xrange(depth):
            if board[i] == col:
                return False

