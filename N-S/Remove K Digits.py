# coding=utf-8
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if num == '' or k < 1:
            return num
        if len(num) == k:
            return '0'
        stack = []
        i = 0
        j = 0
        while j < len(num):
            if stack == []:
                stack.append(num[j])
                j += 1
                continue
            while num[j] < stack[-1]:
                stack.pop()
                i += 1
                if i == k:
                    ans = '' + reduce (lambda x, y: x+y, stack) + num[j:] if stack != [] else num[j:]
                    ans = ans.lstrip ('0')
                    return ans if ans != '' else '0' 
                if stack == []:
                    break
            stack.append(num[j])
            j += 1
        ans = '' + reduce(lambda x, y: x+y, stack[:len(num) - k] ).lstrip('0')
        return ans if ans != '' else '0' 
