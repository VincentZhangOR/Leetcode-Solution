# coding=utf-8
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2 != 0 or len(nums) < 2:
            return False
        nums.sort()
        target = s / 2
        d = collections.defaultdict (set)
        if nums[0] == target:
            return True
        d[0] = {nums[0]}
        for i in xrange(1,len(nums )-1):
            d[i].add(nums[i])
            for x in d[i-1]:
                if x + nums[i] == target:
                    return True
                elif x + nums[i] < target:
                    d[i].add(x +nums[i])
                #print d[i]

