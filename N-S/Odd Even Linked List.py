# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        evenHead=head.next
        odd=head
        even=head.next
        while even and even.next:
            odd.next=odd.next.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=evenHead
        return head
            
