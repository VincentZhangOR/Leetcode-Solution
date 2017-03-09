# coding=utf-8
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 0
        if n%2==0:
            return self .integerReplacement(n /2)+1
        else:
            if self.help(n+1)<self .help(n-1):
                return self .integerReplacement (n+1)+1
            else:
                return self .integerReplacement (n-1)+1
        
    def help(self, n):
        while n%2==0:
            n/=2
        return n
