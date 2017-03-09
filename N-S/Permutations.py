# coding=utf-8
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        ans=[]
        self.dfs(nums,ans,res)
        return res
        
    def dfs(self,lst,ans,res):
        
        if lst==[]:
            res.append(ans+[])
            return
        for i in xrange(len(lst)):
            ans.append(lst[i])
            self.dfs(lst[:i]+lst[i+1:] ,ans,res)
            ans.pop()
