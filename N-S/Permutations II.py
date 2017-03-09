# coding=utf-8
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        res=[]
        self.dfs(nums,ans,res)
        return res
        
    def dfs(self,lst,ans,res):
        if not lst:
            res.append(ans+[])
            return
        for i in xrange(len(lst)):
            if i==0 or lst[i]!=lst[i -1]:
                ans.append(lst[i])
                self.dfs(lst[:i]+lst[i +1:],ans,res)
                ans.pop()
