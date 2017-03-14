class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        if k >= n:
            return s[::-1]
        i = 0
        res = ''
        while True:
            if i + k >= n:
                res += s[i:n][::-1]
                break
            elif i + 2*k >= n:
                res += s[i:i+k][::-1]
                res += s[i+k:n]
                break
            else:
                res += s[i:i+k][::-1]
                res += s[i+k:i+2*k]
                i += 2*k
        return res