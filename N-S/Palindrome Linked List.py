# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next ==None:
            return True
        dummy=ListNode(0)
        dummy.next=head
        slow=fast=dummy
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        new=self.reverse(slow)
        cur1=head
        cur2=new
        while cur1 and cur2:
            if cur1.val!=cur2.val:
                return False
            cur1=cur1.next
            cur2=cur2.next
        return True
        
    def reverse(self, head):
        if not head or not head.next:
            return head
        pre=None
        cur=head
        new=head
        while cur:
            new=cur
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return new
        
