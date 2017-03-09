# coding=utf-8
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n-1
        res = 0
        max = 0
        while left < right-1:
            h = min(height[left], height[right])
            dis = right - left - 1
            if h > max:
                res += dis * (h - max)
                max = h
            if height[left] <= height[right]:
                left += 1
                res -= min (height[left], max )
            else:
                right -= 1
                res -= min
