# coding=utf-8
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if n==0:
            return 0
        dp=[0]*(n+1)
        if s[0]!='0':
            dp[1]=1
        else:
            return 0
        for i in xrange(1,n):
            if s[i]=='0':
                if int(s[i-1])>2 or s[i-1]=='0':
                    return 0
                else:
                    if i>=2:
                        dp[i+1]=min (dp[i],dp[i-1])
                    else:
                        dp[i+1]=dp[i]
            elif int(s[i-1])>2 or (s[i -1]=='2' and int(s[i] )>6) or s[i-1]=='0':
                dp[i+1]=dp[i]
            else:
                dp[i+1]=dp[i]+max(dp[i -1],1)
        return dp[n]
