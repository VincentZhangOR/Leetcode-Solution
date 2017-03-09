# coding=utf-8
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        '''
        n = len(nums)
        if n == 0:
            return []
        if k >= n:
            return [max(nums)]
        pos = -1
        left = 0
        right = k-1
        res = []
        m = float('-inf')
        while right < n:
            if pos == -1:
                #pos = numpy.argmax (nums[:right+1])
                m = max(nums[:right +1])
                pos = 0
                
            elif nums[right] >= m:
                m = nums[right]
            elif m == nums[left-1]:
                m = max(nums[left :right+1])
            
            res.append(m)
            #print left, right, res
            left += 1
            right += 1
            
        return res
        '''
        d = collections.deque()
        n = len(nums)
        res = []
        i = 0
        while i < n:
            while d and nums[d[-1]] <= nums[i]:
                d.pop()
            d.append(i)
            if d[0] == i - k:
                d.popleft()
            if i >= k-1:
                res.append (nums[d[0]])

