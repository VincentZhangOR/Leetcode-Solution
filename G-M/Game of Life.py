# coding=utf-8
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in -place instead.
        """
        m = len(board)
        if m <= 0:
            return
        n = len(board[0])
        row = (1,1,1,0,0,-1,-1,-1)
        col = (1,0,-1,1,-1,1,0,-1)
        
        def help(p,q):
            if p < 0 or q < 0 or p >= m or q >= n:
                return 0
            return board[p][q] & 1
        
        for i in xrange(m):
            for j in xrange(n):
                temp = 0
                for x in xrange(8):
                    temp += help(i +row[x], j+col[x])
                if (board[i][j] == 1 and 2 <= temp <=3) or (board[i][j] == 0 and temp == 3):
                    board[i][j] |= 2
        for i in xrange(m):
            for j in xrange(n):
                board[i][j] >>= 1
