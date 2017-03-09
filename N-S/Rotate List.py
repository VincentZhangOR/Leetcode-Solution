# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==0 or not head:
            return head
        slow=head
        fast=head
        count=0
        while fast and fast.next:
            count+=1
            fast=fast.next
        count+=1
        k%=count
        if k==count:
            return head
        while slow:
            count-=1
            if count==k:
                fast.next=head
                new=slow.next
                slow.next=None
                return new
            slow=slow.next
                
