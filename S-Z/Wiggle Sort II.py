# coding=utf-8
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in -place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        mid = self.findMid(nums, n/2 )
        left = [x for x in nums if x > mid]
        right = [x for x in nums if x < mid]
        middle = [x for x in nums if x == mid]
        ll = len(left)
        lr = len(right)
        lm = len(middle)
        diff = n//2 - ll
        #print left, middle, right, ll, lr, lm, diff
        left += [mid] * diff
        right += [mid] * (lm - diff)
        #print left, right
        for i in xrange(n):
            if i % 2 == 0:
                nums[i] = right[-i/2 -1]
                print right[-i/2-1]
            else:
                nums[i] = left[i//2]
        
        
        
    def findMid(self, nums, k):
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        right = [x for x in nums if x < pivot]
        ll = len(left)
        lr = len(right)
        n = len(nums)
        if k <= ll:
            return self.findMid(left , k)
        if k > n - lr:
            return self.findMid
