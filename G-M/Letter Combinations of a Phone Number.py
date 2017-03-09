# coding=utf-8
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0:
            return []
        res=[]
        d={1:'*',2:'abc',3:'def',4 :'ghi',5:'jkl',6:'mno',7 :'pqrs',8:'tuv',9:'wxyz' ,0:' '}
        return self.dfs(digits, d, '', res)
        
        
    def dfs(self, digits, d, ans, res):
        if len(digits)==0:
            res.append(ans)
            return
        for x in d[int(digits[0])]:
            ans+=x
            self.dfs(digits[1:], d, ans, res)
            ans=ans[:len(ans)-1]

