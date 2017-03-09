# coding=utf-8
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=set()
        ans=0
        for x in s:
            if x in d:
                ans+=2
                d.discard(x)
            else:
                d.add(x)
        return ans+1 if len(d)>0 else ans
