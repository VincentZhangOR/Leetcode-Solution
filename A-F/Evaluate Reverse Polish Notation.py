# coding=utf-8
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for x in tokens:
            if x.isdigit() or x[1:] .isdigit():
                stack.append(int(x))
            else:
                b = stack.pop()
                a = stack.pop()
                if x == '+':
                    c = a + b
                elif x == '-':
                    c = a - b
                elif x == '*':
                    c = a * b
                else:
                    c = a / b
                    if c < 0 and a % b != 0:
                        c += 1
                stack.append(c)
            #print stack
        return stack.pop()
        
