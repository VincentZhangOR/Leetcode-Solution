# coding=utf-8
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return '0'
        s=''
        d={0:'0',1:'1',2:'2',3:'3',4 :'4',5:'5',6:'6',7:'7',8 :'8',9:'9',10:'a',11:'b' ,12:'c',13:'d',14:'e',15 :'f'}
        if num<0:
            num=0xffffffff-(~num)
        while num>0:
            s+=d[num&15]
            num>>=4
        return s[::-1]
            
