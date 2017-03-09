# coding=utf-8
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def getMax(num, n):
            stack = []
            i = 0
            drop = len(num) - n
            if drop == 0:
                return num
            curd = 0
            while i < len(num):
                #print i, num, curd ,drop,stack
                if stack == []:
                    stack.append (num[i])
                    i += 1
                    continue
                while num[i] > stack[ -1]:
                    stack.pop()
                    curd += 1
                    if curd == drop:
                        return stack + num[i:]
                    if stack == []:
                        break
                stack.append(num[i])
                i += 1
            return stack[:n]
            
        def merge(num1, num2):
            i = 0
            j = 0
            m = len(num1)
            n = len(num2)
            res = []
            while i < m and j < n:
                if i == m-1 and j == n -1:
                    break
                temp = max(num1[i] ,num2[j])
                res.append(temp)
                if num1[i:] >= num2[j :]:
                    i += 1
                else:
                    j += 1
                        
                #print i,j,res
            return res
        
        ans = [0 for x in xrange(k)] 
        for i in xrange(max(0,k-len (nums2)), min(k,len(nums1 ))+1):
            #print i
            a = getMax(nums1, i)
            b = getMax(nums2, k-i)
            #print a,b
            ans = max(ans, merge(a +[float('-inf')],b +[float('-inf')]))
        return ans
