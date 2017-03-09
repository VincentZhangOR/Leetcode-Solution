# coding=utf-8
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return []
        d = collections.defaultdict (lambda: 1)
        d[0] = 1
        back = collections.defaultdict (lambda: -1)
        back[0] = -1
        n = len(nums)
        nums.sort()
        
        def topdown(j):
            if j in d:
                return d[j]
            for i in xrange(j):
                temp = topdown(i) + 1 if nums[j] % nums[i] == 0 else 1
                if temp > d[j]:
                    d[j] = temp
                    back[j] = i
            return d[j]
        
        ans = 0
        index = -1
        for i in xrange(n):
            if topdown(i) > ans:
                index = i
                ans = topdown(i)
        
        #print index, d, back
                
        return self.solution(index, back, nums)
        
    def solution(self, index, back, nums):
        if index == -1:
            return []
        #res += nums[index]
        return self.solution (back[index], back, nums) + [nums[index]]
