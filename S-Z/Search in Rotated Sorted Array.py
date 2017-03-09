# coding=utf-8
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        d = collections.defaultdict (lambda: -1)
        for i in xrange(len(nums)):
            d[nums[i]] = i
        return d[target]
            

        '''
        if len(nums)==0:
            return -1
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        left=0
        right=len(nums)-1
        mid=(left+right)/2
        if nums[left]<nums[right]:
            while left<=right:
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
                mid=(left+right)/2
            return -1
        else:
            ans1=self.search(nums[:mid +1], target)
            ans2=self.search(nums[mid +1:],target)
            if ans1==-1 and ans2==-1:
                return -1
            elif ans1==-1:
                return ans2+mid+1
            else:
                return ans1
        '''
