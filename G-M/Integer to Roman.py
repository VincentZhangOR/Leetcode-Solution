# coding=utf-8
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #d = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10 , "V": 5, "I": 1 }
        values =[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ['M', 'CM', 'D', 'CD' ,'C','XC','L','XL', 'X' ,'IX','V','IV','I']
        i=0
        res=''
        while num>0:
            if num>=values[i]:
                num-=values[i]
                res+=roman[i]
            else:
                i+=1
        return res
                
