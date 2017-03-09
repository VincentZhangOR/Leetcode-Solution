# coding=utf-8
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        d={'+','-','*'}
        ans=[]
        for i in xrange(len(input)):
            if input[i] in d:
                left=self .diffWaysToCompute (input[:i])
                right=self .diffWaysToCompute (input[i+1:])
                for l in left:
                    for r in right:
                        ans.append (self.cal(l,r ,input[i]))
        return ans
        
    def cal(self, a, b, x):
        if x=='+':
            return int(a)+int(b)
        elif x=='-':
            return int(a)-int(b)

