# coding=utf-8
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = collections.defaultdict (int)
        for x in s:
            d[x] += 1
        ans = collections.defaultdict (int)
        ans[6] = d['x']
        ans[0] = d['z']
        ans[2] = d['w']
        ans[8] = d['g']
        ans[7] = d['s'] - ans[6]
        ans[4] = d['u']
        ans[5] = d['f'] - ans[4]
        ans[9] = d['i'] - ans[6] - ans[8] - ans[5]
        ans[1] = d['n'] - ans[7] - 2 * ans[9]
        ans[3] = d['t'] - ans[2] - ans[8]
        res = ''
        n = 0
        while n < 10:
            if ans[n] > 0:
                res += (str(n) * ans[n])
            n += 1
        return res
