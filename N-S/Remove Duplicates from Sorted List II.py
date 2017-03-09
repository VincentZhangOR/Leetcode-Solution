# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        dummy=ListNode(0)
        dummy.next=head
        cur=head
        pre=dummy
        while cur and cur.next:
            if cur.val!=cur.next.val:
                pre.next=cur
                pre=pre.next
                cur=cur.next
            else:
                while cur.next and cur .val==cur.next.val:
                    cur=cur.next
                cur=cur.next
                pre.next=cur

        return dummy.next
