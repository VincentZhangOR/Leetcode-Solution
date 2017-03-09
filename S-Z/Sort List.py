# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return head
        fast = head
        slow = head
        temp = head
        while fast and fast.next:
            fast = fast.next.next
            temp = slow
            slow = slow.next
        temp.next = None
        subA = self.sortList(head)
        subB = self.sortList(slow)
        dummy = ListNode(0)
        cur = dummy
        while subA and subB:
            if subA.val <= subB.val:
                cur.next = subA
                subA = subA.next
            else:
                cur.next = subB
                subB = subB.next
            cur = cur.next
        if subA == None:
            cur.next = subB
        if subB == None:
            cur.next = subA
        return dummy.next
