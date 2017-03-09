# coding=utf-8
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[[]]
        for k in xrange(1,len(nums )+1):
            res += self.dfs(k, nums, [], [])
        return res
        
    def dfs(self, k, nums, ans, res ):
        if k==0:
            res.append(ans+[])
            return
        #if nums[0]==pre:
        #    return
        for i in xrange(len(nums)):
            if i>0 and nums[i] ==nums[i-1]:
                continue
            ans.append(nums[i])
            self.dfs(k-1, nums[i+1:] , ans, res)

