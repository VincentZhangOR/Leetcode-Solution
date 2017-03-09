# coding=utf-8
class Solution(object):
    def removeDuplicateLetters(self, s ):
        """
        :type s: str
        :rtype: str
        """
        d = collections.defaultdict (int)
        used = set()
        for i in xrange(len(s)):
            d[s[i]] += 1
        res = []
        for i in xrange(len(s)):
            d[s[i]] -= 1
            if res == [] or (s[i] > res[-1] and s[i] not in used):
                res.append(s[i])
                used.add(s[i])
                continue
            elif s[i] == res[-1]:
                continue
            while s[i] < res[-1]:
                if d[res[-1]] > 0:
                    if s[i] not in used:
                        used.discard (res[-1])
                        res.pop()
                    else:
                        break
                else:
                    break
                if res == []:
                    break
            if s[i] not in used:
                res.append(s[i])
                used.add(s[i])
        ans = ''
        for x in res:
            ans += x
        return ans
                
