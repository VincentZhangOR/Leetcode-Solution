# coding=utf-8
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.dfs(0, target, candidates, [], [])
        
    def dfs(self, start, target, lst, ans, res):
        if target<0:
            return
        if target==0:
            res.append(ans+[])
        for i in xrange(start, len(lst )):
            if i>0 and lst[i]==lst[i -1]:
                continue
            ans.append(lst[i])
            self.dfs(i, target-lst[i], lst[:i]+lst[i+1:], ans , res)
            ans.pop()
        return res
