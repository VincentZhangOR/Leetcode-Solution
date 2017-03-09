# coding=utf-8
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m = len(board)
        if m == 0:
            return 0
        n = len(board[0])
        ans = 0
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] != 'X'):
                    if j == 0 or board[i][j-1] != 'X':
                        ans += 1
                #print i,j,ans
        return ans
