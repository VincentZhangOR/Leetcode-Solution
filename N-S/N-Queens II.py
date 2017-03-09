# coding=utf-8
class Solution(object):
    res = 0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <= 3:
            return 0 if n > 1 else 1
        board = [-1 for x in range(n )]
        self.dfs(0, board,n)
        return self.res
        
    def dfs(self,depth, board,n):
        if depth == n:
            self.res += 1
            return
        for i in xrange(n):
            if self.check(depth, i, board):
                board[depth] = i
                #ans.append('.' * i + 'Q' + '.' * (n - i - 1))
                (self.dfs(depth + 1, board,n))
                #ans.pop()
                board[depth] = -1
        
    def check(self, depth, col, board):
        #print depth, board
        for i in xrange(depth):
            if board[i] == col:
                return False
            if abs(board[i] - col) == abs(depth - i):

