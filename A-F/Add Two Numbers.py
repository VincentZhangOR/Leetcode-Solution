# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0
        l4=ListNode(0)
        res = l4
        while (l1!=None) or (l2!=None) or (flag!=0):
            v1 = ((l1 is None) and [0] or [l1.val])[0]
            v2 = ((l2 is None) and [0] or [l2.val])[0]
            sum = v1 + v2 + flag
            v3 = sum%10
            flag = sum/10
            l4.next=ListNode(v3)
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            l4=l4.next
            #res = l4
        return res.next

