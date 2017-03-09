# coding=utf-8
class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        #c = copy.deepcopy(str)
        n = len(str)
        for i in xrange(1,n):
            if n % i == 0:
                if str[i:] == str[:n -i]:
                    return True
        return False
