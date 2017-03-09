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
        if head==None:
            return None
        if head.next==None:
            return head
        cur=head
        while cur.next:
            
            if cur.val==cur.next.val:
                cur.next=cur.next.next
                
            
            else:
                cur=cur.next
        #if temp.val==cur.val
        return head
                
