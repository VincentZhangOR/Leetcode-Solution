# coding=utf-8
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        d1={}
        #d2={}
        length=len(secret)
        #if length==0:
            #return '0A0B'
        bull=0
        cow=0
        for x,y in zip(secret,guess):
            if x==y:
                bull+=1
                continue
            if x not in d1:
                d1[x]=1
      
            else:
                temp=d1[x]
                d1[x]+=1
                
                if abs(d1[x])<abs(temp ):
                    cow+=1
            if y not in d1:
                d1[y]=-1
        
            else:
                temp=d1[y]
                d1[y]-=1
                
                if abs(d1[y])<abs(temp ):
                    cow+=1
        #for i in d1:
            #print i
            #if d1[i]==0:
                #cow+=1
        return str(bull)+'A'+str(cow )+'B'
