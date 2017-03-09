# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        dummy = ListNode(0)
        cur = head
        dummy.next = cur
        while cur.next:
            if cur.next.val < cur.val:
                pre = dummy
                while cur.next.val > pre.next.val:
                    pre = pre.next
                temp = cur.next
                cur.next = temp.next
                temp.next = pre.next
                pre.next = temp
            else:
                cur = cur.next
        return dummy.next
            
