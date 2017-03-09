# coding=utf-8
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = collections.Counter(s)
        l = [x for x in d if d[x] < k]
        if l ==[]:
            return len(s)
        arr = re.split('|'.join(l),s)
        return max(self .longestSubstring(x,k) for x in arr)
