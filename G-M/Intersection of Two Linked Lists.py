# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cur1=ListNode(0)
        cur2=ListNode(0)
        cur1.next=headA
        cur2.next=headB
        s=set()
        while cur1.next:
            s.add(cur1.next)
            cur1=cur1.next
        while cur2.next:
            if cur2.next in s:
                return cur2.next
            cur2=cur2.next
        return None
