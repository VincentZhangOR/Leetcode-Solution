# coding=utf-8
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s[::-1]
        i=1
        d = { "M": 1000, "D": 500, "C" : 100, "L": 50, "X": 10, "V": 5, "I": 1 }
        ans=d[s[0]]
        
        while i < len(s):
            if d[s[i]]>=d[s[i-1]]:
                ans+=d[s[i]]
            else:
                ans-=d[s[i]]
            i+=1
        return ans
