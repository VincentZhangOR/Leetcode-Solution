# coding=utf-8
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        d = path.split('/')
        curr='/'
        for x in d:
            if x == '..':
                if curr != '/':
                    curr = '/'.join (curr.split('/')[ :-1])
                    if curr=='':
                        curr='/'
            elif x != '.' and x != '':
                if curr != '/':
                    curr += '/'+x
                else:
                    curr += x
        return curr
