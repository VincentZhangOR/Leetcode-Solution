# coding=utf-8
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums=sorted([str(x) for x in nums], cmp=self.compare)
        ans=''.join(nums).lstrip('0')
        return ans or '0'
        
    def compare(self,a,b):
        return [1,-1][a+b>b+a]
