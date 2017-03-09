# coding=utf-8
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in -place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        
        used = set()
        queue = []
        
        def addUsed(i,j):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1 or (i ,j) in used or board[i][j] != 'O':
                return
            used.add((i,j))
            queue.append((i,j))
            
        def bfs():
            while queue:
                i,j = queue.pop()
                addUsed(i-1,j)
                addUsed(i+1,j)
                addUsed(i,j-1)
                addUsed(i,j+1)
            
        for i in xrange(m):
            addUsed(i,0)
            bfs()
            addUsed(i,n-1)
            bfs()
        for j in xrange(n):
            addUsed(0,j)
            bfs()
            addUsed(m-1,j)
            bfs()
        for i in xrange(1,m-1):
            for j in xrange(1,n-1):
                if board[i][j] == 'O' and (i,j) not in used:
                    board[i][j] = 'X'
        return
