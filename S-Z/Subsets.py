# coding=utf-8
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        if not nums:
            return res
        nums.sort()
        for k in xrange(1,len(nums )+1):
            res+=self.help(k,nums,[] ,[])
        return res
        
    def help(self, k, nums, ans, midres):
        if not k:
            midres.append(ans+[])
            return
        n=len(nums)
        for i in xrange(n):
            ans.append(nums[i])
            self.help(k-1,nums[i+1:] ,ans,midres)
            ans.pop()

