# coding=utf-8
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return self.dfs(4, s, '', [])
        
        
    def dfs(self, k, s, ans, res):
        if len(s)<k or len(s)>3*max(k ,1):
            return []
        if len(s)==0 and k==0:
            res.append(ans)
            #ans=[]
            return res
        for i in xrange(0,min(3,len(s ))):
            
            ans+=str(s[i])
            temp=ans.split('.')
            if int(temp[-1])>255 or (len(temp[-1])>1 and temp[-1].startswith ('0')):
                break
            if k>1:
                ans+='.'

            
            self.dfs(k-1, s[i+1:], ans , res)
            if ans[-1]=='.':
                ans=ans[:len(ans)-1]
        return res
