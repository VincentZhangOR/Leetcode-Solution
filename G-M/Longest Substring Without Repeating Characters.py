# coding=utf-8
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = set()
        n=len(s)
        i=0
        j=0
        ans = 0
        while i<n and j<n:
            if s[i] not in res:
                res.add(s[i])
                i += 1
                ans = max(ans,i-j)
                #print "ans:",ans
            else:
                res.remove(s[j])
                j += 1
                #res.add(s[i])
        return ans
