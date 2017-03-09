# coding=utf-8
class Solution(object):
    def longestValidParentheses(self , s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        d = collections.defaultdict (int)
        stack = []
        pre = -1
        for i in xrange(n):
            if s[i] == '(':
                d[i] = d[i-1]
                stack.append(i)
            else:
                if len(stack) > 0:
                    stack.pop()
                    if len(stack) == 0:
                        d[i] = max (d[i-1], i-pre)
                    else:
                        d[i] = max (d[i-1], i-stack[ -1])
                else:
                    pre = i

