# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = head
        pre = dummy
        for i in xrange(m-1):
            pre.next = cur
            cur = cur.next
            pre = pre.next
        start = None
        end = cur
        temp = None
        for i in xrange(m, n+1):
            temp = cur.next
            cur.next = start
            start = cur
            cur = temp
        pre.next = start
        end.next = temp
        return dummy.next
