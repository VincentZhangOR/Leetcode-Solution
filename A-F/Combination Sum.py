# coding=utf-8
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.dfs(target, 0, candidates, [],[])
        
    def dfs(self, target, start, lst, ans, res):
        if target<0:
            return
        if target==0:
            res.append(ans+[])
            return
        for i in xrange(start,len(lst )):
            ans.append(lst[i])
            self.dfs(target-lst[i], i, lst, ans, res)
            ans.pop()
        return res
