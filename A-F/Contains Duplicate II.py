# coding=utf-8
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d={}
        for i,x in zip(range(len(nums )),nums):
            if x not in d:
                d[x]=i
            else:
                if i-d[x]<=k:
                    return True
                else:
                    d[x]=i
        return False
