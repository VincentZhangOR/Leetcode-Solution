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
        ans1 = 0
        ans2 = 0
        while l1:
            ans1 *= 10
            ans1 += l1.val
            l1 = l1.next
        while l2:
            ans2 *= 10
            ans2 += l2.val
            l2 = l2.next
        ans = ans1 + ans2
        dummy = ListNode(0)
        cur = dummy
        for x in str(ans):
            cur.next = ListNode(int (x))
            cur = cur.next
        cur.next = None

