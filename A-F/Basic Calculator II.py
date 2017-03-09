# coding=utf-8
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = re.sub(r'\d+', ' \g<0> ' , s)
        op = {'+': operator.add, '-' : operator.sub, '*': operator.mul, '/': operator.floordiv}
        expressions = s.split()
        ans = cur = index = 0
        f = op['+']
        while index < len (expressions):
            e = expressions[index]
            if e in '+-':
                ans = f(ans, d)
                f = op[e]
            elif e in '*/':
                index += 1
                d = op[e](d, int (expressions[index ]))
            else:
                d = int(e)
            index += 1

