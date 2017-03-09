# coding=utf-8
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        s = 0
        right = sum(nums)
        left = right / m
        while left < right:
            count = m
            flag = 0
            mid = (left + right) / 2
            s = 0
            for i in xrange(n):
                if nums[i] > mid:
                    flag = 1
                    break
                if s + nums[i] > mid:
                    count -= 1
                    s = 0
                s += nums[i]
                if count == 0:
                    flag = 1
                    break
            if flag == 0:
                right = mid
            else:
                left = mid + 1
        return left
