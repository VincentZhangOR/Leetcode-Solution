# coding=utf-8
class Solution(object):
    def wordPattern(self, pattern, str ):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        b=str.split()
        return map(pattern.find ,pattern)==map(b.index,b)
