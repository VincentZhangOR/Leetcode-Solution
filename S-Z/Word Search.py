# coding=utf-8
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board==None or board==[]:
            return False
        for i in xrange(len(board)):
            for j in xrange(len (board[0])):
                if self.dfs(board, word, 0, False, i, j)==True:
                    return True
        return False
        
    def dfs(self, board, word, k, ans, i, j):
        
        if board[i][j]==word[k]:
            if k==len(word)-1:
                return True
            temp=board[i][j]
            board[i][j]='*'
            if i>0:
                ans = self.dfs(board, word, k+1, False, i -1, j)
            if ans==False and i<len (board)-1:
                ans = self.dfs(board, word, k+1, False, i +1, j)
            if ans==False and j>0:
                ans = self.dfs(board, word, k+1, False, i , j-1)
            if ans==False and j<len (board[0])-1:
                ans = self.dfs(board, word, k+1, False, i , j+1)
            board[i][j]=temp
        return ans
