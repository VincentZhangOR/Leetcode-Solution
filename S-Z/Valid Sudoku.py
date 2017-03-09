# coding=utf-8
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        d=set()
        for x in board:
            d=set()
            for y in x:
                if y=='.':
                    continue
                if y not in d:
                    d.add(y)
                else:
                    return False
        for i in xrange(9):
            d=set()
            for j in xrange(9):
                if board[j][i]=='.':
                    continue
                if board[j][i] not in d:
                    d.add (board[j][i])
                else:
                    return False
        for n in xrange(0,9,3):
            for m in xrange(0,9,3):
                d=set()
                for i in xrange(3):
                    for j in xrange (3):
                        if board[i +m][j+n]=='.':
                            continue
                        if board[i +m][j+n] not in d:
                            d.add (board[i+m][j+n])
                        else:
                            return False
        return True

